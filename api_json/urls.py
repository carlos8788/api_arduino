from django.urls import path
from .views import ArduinoView

urlpatterns=[
    path('tarjetas/', ArduinoView.as_view(), name='tarjetas_lista'),
    path('tarjetas/<id_arduino>', ArduinoView.as_view(), name='tarjeta')
]