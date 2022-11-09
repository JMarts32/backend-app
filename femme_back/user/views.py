from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NombreSerializer
from .models import Nombre


"""
Se usa el framwork REST para facilitar el uso de la visualizacion de jsons
y poder usar los decoradores para los usos de las API'S
"""
@api_view(["GET"])
def getRoute(request):
    # Es un json con las rutas que vamos a usar dentro del proyecto
    routes = [
        {
            'Endpoint': '',
            'method': '',
            'body': None,
            'description': ''
        },
    ]
    return Response(routes)


"""
Serializamos para poder obtener la informacion en JSON's
"""
@api_view(['GET'])
def getNombres(request):
    nombres = Nombre.objects.all()
    serializer = NombreSerializer(nombres, many=True)
    return  Response(serializer.data)