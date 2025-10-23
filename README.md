# 🏏 IPL Win Prediction

<div align="center">

![IPL](https://img.shields.io/badge/IPL-Win_Prediction-blue?style=for-the-badge&logo=cricket&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
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
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [Contact](#contact)

---

## 🎯 About The Project

An **IPL Match Prediction System** powered by Machine Learning that predicts the winning team based on critical match factors. This project analyzes historical IPL data to provide real-time win probability predictions for ongoing matches.

### Key Prediction Factors:
- 🏏 **Batting Team** - Current batting side
- 🎳 **Bowling Team** - Current bowling side  
- 🏟️ **Venue** - Match location and ground conditions
- 🪙 **Toss Results** - Toss winner and decision
- 📊 **Match Situation** - Current score, wickets, and overs

The model uses advanced machine learning algorithms to analyze these factors and predict match outcomes with high accuracy.

---

## ✨ Features

- ⚡ **Real-time Predictions** - Get instant win probability predictions
- 🎯 **High Accuracy** - Trained on extensive historical IPL data
- 🌐 **Web Deployment** - Accessible via Hugging Face Spaces
- 📊 **Interactive UI** - User-friendly interface for easy predictions
- 🔄 **Live Updates** - Predictions update based on match progress
- 📈 **Data Visualization** - Visual representation of win probabilities

---

## 🛠️ Built With

### Core Technologies
- ![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white) - Primary programming language
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) - Data manipulation and analysis
- ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) - Machine learning algorithms
- ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) - Numerical computations

### Deployment
- ![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat&logo=huggingface&logoColor=black) - Model deployment platform
- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) - Web application framework

---

## 🚀 Demo

### 🌐 Live Application
Try out the live prediction model here:  
👉 **[IPL Win Probability Predictor](https://huggingface.co/spaces/Arghadeep007/ipl-win-probability)**

### 📸 Screenshots
![Demo Screenshot](https://via.placeholder.com/800x400?text=Add+Your+Screenshot+Here)

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

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

---

## 📖 Usage

### Using the Web Interface

1. Visit the [live demo](https://huggingface.co/spaces/Arghadeep007/ipl-win-probability)
2. Select the **batting team** and **bowling team**
3. Choose the **venue** from the dropdown
4. Enter **toss details** (winner and decision)
5. Input current **match situation** (runs, wickets, overs)
6. Click **Predict** to get win probability

### Using the Python API

```python
from ipl_predictor import IPLPredictor

# Initialize the predictor
predictor = IPLPredictor()

# Make prediction
result = predictor.predict(
    batting_team='Mumbai Indians',
    bowling_team='Chennai Super Kings',
    venue='Wankhede Stadium',
    toss_winner='Mumbai Indians',
    toss_decision='bat'
)

print(f"Win Probability: {result['probability']}%")
```

---

## 🧠 Model Details

### Algorithm
- **Model Type**: Logistic Regression / Random Forest Classifier
- **Training Data**: Historical IPL matches (2008-2024)
- **Features**: 15+ engineered features
- **Accuracy**: ~85% on test data

### Feature Engineering
- Team performance metrics
- Venue-specific win rates
- Toss impact analysis
- Head-to-head statistics
- Player form indicators

### Model Training Pipeline
```
Data Collection → Preprocessing → Feature Engineering → Model Training → Evaluation → Deployment
```

---

## 📊 Dataset

The model is trained on comprehensive IPL data including:
- 📅 **Seasons**: 2008-2024
- 🏏 **Matches**: 1000+ matches
- 🏟️ **Venues**: All major IPL stadiums
- 👥 **Teams**: All IPL franchises

**Data Sources:**
- Official IPL statistics
---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn and create. Any contributions you make are **greatly appreciated**!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📞 Contact

**Your Name** - Arghadeep nandi 
**email** - arghadeepnandi93@gmail.com

**Project Link**: (https://github.com/arghadeepnandi/ipl-win-prediction)

**Live Demo**: [https://huggingface.co/spaces/Arghadeep007/ipl-win-probability](https://huggingface.co/spaces/Arghadeep007/ipl-win-probability)

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙏 Acknowledgments

- [IPL Official Website](https://www.iplt20.com/)
- [Hugging Face Spaces](https://huggingface.co/spaces)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

<div align="center">

### ⭐ Don't forget to star this repo if you found it helpful! ⭐

Made with ❤️ by [Arghadeep Nandi]

</div>
