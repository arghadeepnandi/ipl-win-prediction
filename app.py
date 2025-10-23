from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# ---- change these lists if you want ----
teams = sorted([
    'Sunrisers Hyderabad','Mumbai Indians','Royal Challengers Bangalore',
    'Kolkata Knight Riders','Kings XI Punjab','Chennai Super Kings',
    'Rajasthan Royals','Delhi Capitals'
])

cities = sorted([
    'Hyderabad','Bangalore','Mumbai','Indore','Kolkata','Delhi','Chandigarh',
    'Jaipur','Chennai','Cape Town','Port Elizabeth','Durban','Centurion',
    'East London','Johannesburg','Kimberley','Bloemfontein','Ahmedabad',
    'Cuttack','Nagpur','Dharamsala','Visakhapatnam','Pune','Raipur','Ranchi',
    'Abu Dhabi','Sharjah','Mohali','Bengaluru'
])

# Load your model (can be a plain classifier or a full sklearn pipeline)
model = pickle.load(open('pipe.pkl', 'rb'))

# Build a preprocessor to match what the model expects.
# If your model is a full pipeline containing preprocessing, skip preprocess step and call model.predict_proba on raw input.
cat_cols = ['batting_team', 'bowling_team', 'city']
num_cols = ['runs_left','balls_left','wickets','total_runs_x','crr','rrr']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
    ('num', StandardScaler(), num_cols)
])

# Fit the preprocessor on representative dummy data so it can transform single inputs.
# IMPORTANT: these values should include all categorical categories used in training.
dummy = pd.DataFrame({
    'batting_team': teams,
    'bowling_team': teams,
    'city': cities[:len(teams)],    # some matching length for combining
    'runs_left': [50]*len(teams),
    'balls_left': [60]*len(teams),
    'wickets': [5]*len(teams),
    'total_runs_x': [160]*len(teams),
    'crr': [7.5]*len(teams),
    'rrr': [8.0]*len(teams)
})
preprocessor.fit(dummy)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', teams=teams, cities=cities)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        batting_team = request.form['batting_team']
        bowling_team = request.form['bowling_team']
        city = request.form['city']
        target = float(request.form['target'])
        score = float(request.form['score'])
        overs = float(request.form['overs'])
        wickets_out = float(request.form['wickets'])

        if overs == 0:
            return render_template('index.html', teams=teams, cities=cities,
                                   error="Overs cannot be 0 while calculating run rate.")

        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets_out
        crr = score / overs
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets_left],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })
        # If model is a pipeline that already includes preprocessing, directly predict:
        try:
            proba = model.predict_proba(input_df)
        except Exception:
            # Otherwise preprocess then predict
            X_proc = preprocessor.transform(input_df)
            proba = model.predict_proba(X_proc)

        loss = proba[0][0]
        win = proba[0][1]

        return render_template('index.html', teams=teams, cities=cities,
                               result=True,
                               batting_team=batting_team,
                               bowling_team=bowling_team,
                               win_pct=round(win*100,2),
                               loss_pct=round(loss*100,2),
                               inputs=input_df.to_dict(orient='records')[0])

    except Exception as e:
        return render_template('index.html', teams=teams, cities=cities, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)