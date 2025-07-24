## Model Training / RandomForestClassifier
Before running the prediction or testing scripts, you must train the machine learning model first to generate the model.pkl file.

Steps to train the model
Prepare your training dataset.

Run the training script (e.g., train_model.py).

This will create the serialized model file ml_model/model.pkl.

Once the model file is created, you can run the prediction/testing scripts.

## Requirements
Make sure you have Python 3.x installed.

Install the required Python packages with:

bash
Copier
Modifier
pip install -r requirements.txt
Note: The model.pkl file is not included in the repository due to its size.
Please train the model locally or obtain the pre-trained model file before testing.

## JWT Authentication
This project uses JWT (JSON Web Token) for authentication to secure the API endpoints. Users must authenticate to access protected routes such as the prediction API.

Authentication Workflow
1. Register a new user (if you don’t have an account):
URL: /api/auth/registration/

Method: POST

Body (JSON):

json
Copier
Modifier
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password1": "your_password",
  "password2": "your_password"
}
2. Login to get access and refresh tokens:
URL: /api/auth/login/

Method: POST

Body (JSON):

json
Copier
Modifier
{
  "email": "user@example.com",
  "password": "your_password"
}
3. Refresh JWT token:
URL: /api/auth/jwt/refresh/

Method: POST

Body (JSON):

json
Copier
Modifier
{
  "refresh": "your_refresh_token_here"
}
Prediction API
The prediction endpoint requires a POST request with the following JSON body:

URL: /api/predict

Method: POST

Body (JSON):

json
Copier
Modifier
{
  "age": 70,
  "height_cm": 165,
  "weight_kg": 65,
  "waist_cm": 89,
  "eyesight_left": 0.6,
  "eyesight_right": 0.7,
  "hearing_left": 2,
  "hearing_right": 2,
  "systolic": 146,
  "relaxation": 83,
  "fasting_blood_sugar": 147,
  "Cholesterol": 194,
  "triglyceride": 55,
  "HDL": 57,
  "LDL": 126,
  "hemoglobin": 16.2,
  "Urine_protein": 1,
  "serum_creatinine": 1.1,
  "AST": 27,
  "ALT": 23,
  "Gtp": 37,
  "dental_caries": 1
}
