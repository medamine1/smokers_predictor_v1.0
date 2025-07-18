from rest_framework.decorators import api_view
from rest_framework.response import Response
import joblib
import numpy as np

# Load your model
model = joblib.load('ml_model/model.pkl')

@api_view(['POST'])
def predict(request):
    try:
        data = request.data
        features = [
            data.get("age"),
            data.get("height_cm"),
            data.get("weight_kg"),
            data.get("waist_cm"),
            data.get("eyesight_left"),
            data.get("eyesight_right"),
            data.get("hearing_left"),
            data.get("hearing_right"),
            data.get("systolic"),
            data.get("relaxation"),
            data.get("fasting_blood_sugar"),
            data.get("Cholesterol"),
            data.get("triglyceride"),
            data.get("HDL"),
            data.get("LDL"),
            data.get("hemoglobin"),
            data.get("Urine_protein"),
            data.get("serum_creatinine"),
            data.get("AST"),
            data.get("ALT"),
            data.get("Gtp"),
            data.get("dental_caries")
        ]


        if None in features:
            return Response({"error": "Missing one or more input features"}, status=400)

        input_array = np.array([features])
        prediction = model.predict(input_array)[0]
        proba = model.predict_proba(input_array)[0]

        result = "Smoker" if prediction == 1 else "Non-smoker"
        confidence = round(proba[prediction] * 100, 2)

        return Response({"result": result, "confidence": confidence})

    except Exception as e:
        return Response({"error": str(e)}, status=500)
