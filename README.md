# 🧪 Diabetes Prediction 

This project is a machine learning-based web application that predicts whether a person is likely to have diabetes based on their health metrics. It uses the Pima Indians Diabetes Dataset and is deployed using Flask.

---

## 🚀 Features

- Predicts diabetes (positive/negative) using user input
- Trained using standard ML models 
- Simple and responsive web form interface
- Easily deployable with Flask
- Extendable for cloud deployment (Heroku, Render, etc.)

---

## 🧠 Machine Learning

- **Algorithm Used**: KNN
- **Evaluation Metrics**: Accuracy, Confusion Matrix, Precision/Recall
- **Preprocessing**:
  - Handling missing values (0s replaced with NaN)
  - Feature scaling (optional)
  - Train-test split

---

## 📊 Input Features

| Feature                   | Description                       |
|--------------------------|-----------------------------------|
| Pregnancies              | Number of pregnancies             |
| Glucose                  | Glucose level                     |
| BloodPressure            | Blood pressure                    |
| SkinThickness            | Skin fold thickness               |
| Insulin                  | Serum insulin level               |
| BMI                      | Body Mass Index                   |
| DiabetesPedigreeFunction | Family history of diabetes        |
| Age                      | Age of the person                 |

---

## 💻 Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/diabetes-prediction.git
cd diabetes-prediction
```
2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```
3. **Insatll dependencies**
```bash
pip install -r requirements.txt
```
4.**Run the app**
```bash
python app.py
```
Open http://127.0.0.1:5000 in your browser.



