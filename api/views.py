from rest_framework import viewsets
from diary.models import Thought
from .serializers import ThoughtSerializer
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import os
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class ThoughtViewSet(viewsets.ModelViewSet):
    queryset = Thought.objects.all()
    serializer_class = ThoughtSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['GET'])
def weather_lookup(request):
    city = request.query_params.get('city')

    if not city:
        return Response({'error': 'city parameter is required'}, status=400)

    key = os.getenv('WEATHER_API_KEY')

    response = requests.get(
        f'http://api.weatherapi.com/v1/current.json?key={key}&q={city}')

    if response.status_code == 200:
        result = response.json()

        return Response({'city': city,
                         'temp_c': result['current']['temp_c'],
                         'temp_f': result['current']['temp_f'],
                         'wind_kph': result['current']['wind_kph'],
                         'humidity': result['current']['humidity'],
                         'condition': result['current']['condition']['text'],
                         'last_updated': result['current']['last_updated']
                         })
    else:
        return Response({'error': 'city not found'}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_lookup(request):
    user = request.user

    return Response({
        'username': user.username,
        'email': user.email,
        'city': user.city
    })
