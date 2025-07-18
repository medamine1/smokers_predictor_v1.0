from django.shortcuts import render
from .forms import PredictForm
from ml_model.utils import predict

def predict_view(request):
    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
         input_data = form.cleaned_data
         result, probability = predict(input_data)  
         print(f"Prediction: {result}, Probability: {probability}")
         return render(request, 'predictor/result.html', {
                'result': result,       
                'probability': probability*100, 
                'form': form
            })    
       
    else:
         form = PredictForm()

         return render(request, 'predictor/index.html', {'form': form})
