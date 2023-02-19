from django.views import View
from .models import Arduino
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class ArduinoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_arduino=''):
        print(id_arduino, '***'*10)
        if len(id_arduino)>0:
            tarjetas=list(Arduino.objects.filter(id_arduino=id_arduino).values())
            print(tarjetas, '***'*10)
            if len(tarjetas)>0:
                tarjeta = tarjetas[0]
                dato = {'tarjeta': tarjeta}
                return JsonResponse(dato)
            else:
                dato = {'tarjeta': 'no fount'}
                return JsonResponse(dato)
        else:
            tarjetas = list(Arduino.objects.values())
            if len(tarjetas)>0:
                datos = {'tarjetas': tarjetas}
            # if len(tarjetas)>0:
            #     datos = {'message': 'succes', 'tarjetas': tarjetas}
            else:
                datos = {'message': 'vacio'}
            return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass