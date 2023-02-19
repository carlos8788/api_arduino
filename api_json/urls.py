from django.urls import path
from .views import ArduinoView

urlpatterns=[
    path('tarjetas/', ArduinoView.as_view(), name='tarjetas_lista')
]