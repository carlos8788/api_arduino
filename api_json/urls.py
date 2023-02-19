from django.urls import path
from .views import ArduinoView, home

urlpatterns=[
    path('tarjetas/', ArduinoView.as_view(), name='tarjetas'),
    path('tarjetas/<id_arduino>', ArduinoView.as_view(), name='tarjeta'),
    
]