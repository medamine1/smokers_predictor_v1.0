from django.urls import path
from . import views
from .views import predict

urlpatterns = [
    path('api/predict/',views.predict, name='predict'),
    path('api/hello/', views.HelloView.as_view(), name='hello'),
]
