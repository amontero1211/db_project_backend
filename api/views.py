from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import ArtWork, Artist
from django.contrib.auth.models import User
from .serializers import ArtWorkSerializer, ArtistSerializer, PurchaserSerializer
from django.utils.html import format_html
from datetime import datetime
import re

@api_view(['GET'])
def get_artworks(request):
    artWork = ArtWork.objects.all()
    serializers = ArtWorkSerializer(artWork, many=True)
    serializers.data
    return Response(serializers.data)

@api_view(['GET'])
def get_artwork(request, id):
    artWork = ArtWork.objects.get(id=id)
    serializers = ArtWorkSerializer(artWork)
    serializers.data
    return Response(serializers.data)


@api_view(['POST'])
def post_user(request):

    print('\n-------------------------------------------------\n')
    print(request.data)
    print('\n-------------------------------------------------\n')

    user = User.objects.create_user(
        username=request.data['user'],
        email=request.data['email'],
        password=request.data['password']
    )

    print(user)

    # new_user = {
    #     'username': re.sub(' ','_',request.data['user']),
    #     'email': request.data['email'],
    #     'name': request.data['name'],
    #     'password': request.data['password'],
    #     'card_number': request.data['creditcardnumber'],
    #     'card_back_number': request.data['BackNumbers'],
    #     'card_expiration_date': request.data['ExpDate'],
    #     'purchase_key': '321123',
    #     'question_1': request.data['pregunta1'],
    #     'question_2': request.data['pregunta2'],
    #     'question_3': request.data['pregunta3'],        
    #     'answer_1': 'request.data.pregunta1',
    #     'answer_2': 'request.data.pregunta2',
    #     'answer_3': 'request.data.pregunta3',       
    # }

    
    # if user.is_valid():
    #     user.save()

    return Response(request.data)

@api_view(['GET'])
def get_artists(request):
    artists = Artist.objects.all()
    serializers = ArtistSerializer(artists, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def get_artist(request, id):
    artists = Artist.objects.get(id=id)
    serializers = ArtistSerializer(artists)
    return Response(serializers.data)
