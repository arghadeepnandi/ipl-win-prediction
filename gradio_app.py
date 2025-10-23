import pickle
import pandas as pd
import gradio as gr
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# ---- Lists of teams and cities ----
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]
cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh',
    'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
    'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad',
    'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi',
    'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru'
]

# ---- Load trained model ----
model = pickle.load(open('pipe.pkl', 'rb'))

# ---- Preprocessor (same as Flask version) ----
cat_cols = ['batting_team', 'bowling_team', 'city']
num_cols = ['runs_left', 'balls_left', 'wickets', 'total_runs_x', 'crr', 'rrr']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
    ('num', StandardScaler(), num_cols)
])

dummy = pd.DataFrame({
    'batting_team': teams,
    'bowling_team': teams,
    'city': cities[:len(teams)],
    'runs_left': [50] * len(teams),
    'balls_left': [60] * len(teams),
    'wickets': [5] * len(teams),
    'total_runs_x': [160] * len(teams),
    'crr': [7.5] * len(teams),
    'rrr': [8.0] * len(teams)
})
preprocessor.fit(dummy)


# ---- Prediction Function ----
def predict(batting_team, bowling_team, city, target, score, overs, wickets_out):
    if overs == 0:
        return "Overs cannot be 0 while calculating run rate."

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

    try:
        proba = model.predict_proba(input_df)
    except Exception:
        X_proc = preprocessor.transform(input_df)
        proba = model.predict_proba(X_proc)

    loss = proba[0][0]
    win = proba[0][1]
    return f"🏏 {batting_team} Win Probability: {round(win * 100, 2)}%\n🧤 {bowling_team} Win Probability: {round(loss * 100, 2)}%"


# ---- Gradio UI ----
iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Dropdown(teams, label="Batting Team"),
        gr.Dropdown(teams, label="Bowling Team"),
        gr.Dropdown(cities, label="City"),
        gr.Number(label="Target"),
        gr.Number(label="Current Score"),
        gr.Number(label="Overs Completed"),
        gr.Number(label="Wickets Fallen")
    ],
    outputs="text",
    title="🏏 IPL Win Probability Predictor",
    description="Predict win probabilities based on live match conditions."
)

iface.launch()
