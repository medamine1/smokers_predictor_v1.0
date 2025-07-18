from utils import predict

samples = [

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
]


for test_person in samples:

 prediction, proba = predict(test_person)
 print(f"Prediction: {'Smoker' if prediction == 1 else 'Non-smoker'}")
 print(f"confidence: {proba:.2%}")
