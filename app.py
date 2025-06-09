from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load('knn_diabetes_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # This will be your input form page

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form or JSON
    data = request.form  # or request.json if using API calls
    
    # Extract features and convert to the right format (list or numpy array)
    features = [float(data.get(feature)) for feature in ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
    
    features = np.array(features).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features)
    output = prediction[0]
    
    # Return result
    if output == 1:
        result = "The model predicts diabetes positive."
    else:
        result = "The model predicts diabetes negative."
        
    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
