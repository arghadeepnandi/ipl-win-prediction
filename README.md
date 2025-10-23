# 🏏 IPL Win Prediction

<div align="center">

![IPL](https://img.shields.io/badge/IPL-Win_Prediction-blue?style=for-the-badge&logo=cricket&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Hugging Face](https://img.shields.io/badge/🤗_Hugging_Face-FFD21E?style=for-the-badge)

### 🎯 Predict IPL Match Winners with Machine Learning

**[Live Demo](https://huggingface.co/spaces/Arghadeep007/ipl-win-probability)** • **[Report Bug](https://github.com/YourUsername/ipl-win-prediction/issues)** • **[Request Feature](https://github.com/YourUsername/ipl-win-prediction/issues)**

</div>

---

## 📋 Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Built With](#built-with)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Contact](#contact)

---

## 🎯 About The Project

An **IPL Match Prediction System** powered by Machine Learning that predicts the winning team based on critical match factors. This project analyzes historical IPL data to provide real-time win probability predictions for ongoing matches.

### Key Prediction Factors:
- 🏏 **Batting Team** - Current batting side
- 🎳 **Bowling Team** - Current bowling side  
- 🏟️ **Venue/City** - Match location and ground conditions
- 🎯 **Target Score** - Total runs to chase
- 📊 **Current Score** - Runs scored so far
- ⏱️ **Overs Completed** - Current over progress
- 🚫 **Wickets Lost** - Number of wickets down

The model calculates crucial metrics like **Current Run Rate (CRR)** and **Required Run Rate (RRR)** to predict match outcomes with high accuracy.

---

## ✨ Features

- ⚡ **Real-time Predictions** - Get instant win probability predictions during live matches
- 🎯 **Dynamic Calculations** - Automatically computes CRR, RRR, runs left, and balls left
- 🌐 **Web Interface** - Clean and intuitive Flask-based web application
- 📊 **Probability Display** - Shows win percentage for both batting and bowling teams
- 🔄 **Live Updates** - Predictions update based on current match situation
- 🏟️ **Multi-Venue Support** - Supports 29+ IPL venues including international locations
- 🏏 **All Teams Covered** - Includes all major IPL franchises

---

## 🛠️ Built With

### Core Technologies
- ![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white) - Primary programming language
- ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) - Web application framework
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) - Data manipulation and analysis
- ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) - Machine learning algorithms
- ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) - Numerical computations

### Machine Learning Components
- **OneHotEncoder** - Categorical feature encoding
- **StandardScaler** - Feature normalization
- **ColumnTransformer** - Feature preprocessing pipeline
- **Pickle** - Model serialization

### Deployment
- ![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat&logo=huggingface&logoColor=black) - Model deployment platform

---

### 🌐 Live Application
Try out the live prediction model here:  
👉 **[IPL Win Probability Predictor](https://huggingface.co/spaces/Arghadeep007/ipl-win-probability)**

### Supported Teams
- Sunrisers Hyderabad
- Mumbai Indians
- Royal Challengers Bangalore
- Kolkata Knight Riders
- Kings XI Punjab
- Chennai Super Kings
- Rajasthan Royals
- Delhi Capitals

### Supported Venues
29+ cities including: Hyderabad, Bangalore, Mumbai, Delhi, Chennai, Kolkata, Jaipur, Pune, Abu Dhabi, Sharjah, and more!

---

## 💻 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YourUsername/ipl-win-prediction.git
   cd ipl-win-prediction
   ```

2. **Create a virtual environment** (Optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure model file exists**
   Make sure `pipe.pkl` (trained model) is in the project root directory

5. **Run the Flask application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://127.0.0.1:5000`

---

## 📖 Usage

### Using the Web Interface

1. Visit the application at `http://127.0.0.1:5000` (local) or the [live demo](https://huggingface.co/spaces/Arghadeep007/ipl-win-probability)
2. **Select Batting Team** - Choose the team currently batting
3. **Select Bowling Team** - Choose the team currently bowling
4. **Select City** - Pick the venue where match is being played
5. **Enter Target** - Input the total runs to chase
6. **Enter Current Score** - Input runs scored by batting team
7. **Enter Overs** - Input overs completed (e.g., 15.4)
8. **Enter Wickets** - Input number of wickets lost
9. Click **Predict Probability** to get results

### Example Input
```
Batting Team: Mumbai Indians
Bowling Team: Chennai Super Kings
City: Mumbai
Target: 180
Score: 120
Overs: 15.0
Wickets: 4
```

### Example Output
```
Mumbai Indians Win Probability: 65.43%
Chennai Super Kings Win Probability: 34.57%
```

---

## 🧠 Model Details

### Algorithm & Architecture
- **Model Type**: Scikit-learn Pipeline with Logistic Regression/Random Forest
- **Preprocessing**: 
  - OneHotEncoder for categorical features (teams, cities)
  - StandardScaler for numerical features
  - ColumnTransformer for unified preprocessing

### Features Used
#### Categorical Features:
- `batting_team` - Current batting team
- `bowling_team` - Current bowling team
- `city` - Match venue

#### Numerical Features:
- `runs_left` - Runs needed to win
- `balls_left` - Balls remaining (120 - overs*6)
- `wickets` - Wickets remaining (10 - wickets_out)
- `total_runs_x` - Target score
- `crr` - Current Run Rate (score/overs)
- `rrr` - Required Run Rate ((runs_left*6)/balls_left)

### Feature Engineering
The model automatically calculates:
```python
runs_left = target - score
balls_left = 120 - (overs * 6)
wickets_left = 10 - wickets_out
crr = score / overs
rrr = (runs_left * 6) / balls_left
```

### Model Training Pipeline
```
Raw Data → Feature Engineering → Preprocessing (OneHot + Scaling) → Model Training → Pickle Serialization
```

---

## 📊 Dataset

The model is trained on comprehensive IPL data including:
- 📅 **Historical Matches**: Multiple IPL seasons
- 🏏 **Match Scenarios**: Various score situations and outcomes
- 🏟️ **Venues**: 29+ different cities and stadiums
- 👥 **Teams**: All major IPL franchises
- 📈 **Features**: Team performance, venue statistics, match situation metrics

---

## 📁 Project Structure

```
ipl-win-prediction/
│
├── app.py                 # Flask application
├── pipe.pkl              # Trained ML model (pickle file)
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
│
├── templates/
│   └── index.html       # Web interface template
│
├── static/              # CSS
│   ├── css/
│
│
└── notebooks/           # Jupyter notebooks (optional)
    └── model_training.ipynb
```

---

## 🔧 Dependencies

Create a `requirements.txt` file with:
```
Flask==2.3.0
pandas==2.0.0
numpy==1.24.0
scikit-learn==1.3.0
pickle5==0.0.12
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn and create. Any contributions you make are **greatly appreciated**!

### How to Contribute:

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Ideas for Contribution:
- 🎨 Improve UI/UX design
- 📊 Add data visualizations
- 🔄 Update team/venue lists
- 🧪 Add unit tests
- 📈 Improve model accuracy
- 📝 Enhance documentation

---

## 📞 Contact

**Name** - Arghadeep Nandi 
**Email** - arghadeepnandi93@gmail.com

**Project Link**: (https://github.com/arghadeepnandi/ipl-win-prediction)

**Live Demo**: [https://huggingface.co/spaces/Arghadeep007/ipl-win-probability](https://huggingface.co/spaces/Arghadeep007/ipl-win-probability)

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙏 Acknowledgments

- [IPL Official Website](https://www.iplt20.com/) - Official IPL data source
- [Scikit-learn Documentation](https://scikit-learn.org/) - Machine learning library
- [Flask Documentation](https://flask.palletsprojects.com/) - Web framework
- [Hugging Face Spaces](https://huggingface.co/spaces) - Deployment platform
- [Kaggle IPL Datasets](https://www.kaggle.com/datasets) - Training data

---

## 🚀 Future Enhancements

- [ ] Add player-specific statistics
- [ ] Include weather conditions
- [ ] Real-time score integration via API
- [ ] Historical head-to-head analysis
- [ ] Mobile application development
- [ ] Multi-language support

---

<div align="center">

### ⭐ Don't forget to star this repo if you found it helpful! ⭐

Made with ❤️ and 🏏 by [Arghadeep Nandi]

</div>
