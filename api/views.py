from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import ArtWork
from .serializers import ArtWorkSerializer

@api_view(['GET'])
def get_artworks(request):
    artWork = ArtWork.objects.all()
    serializers = ArtWorkSerializer(artWork, many=True)
    return Response(serializers.data)


@api_view(['POST'])
def potsData(request):
    artWork = ArtWorkSerializer(data=request.data)
    
    if artWork.is_valid():
        artWork.save()
    
    return Response(artWork.data)
