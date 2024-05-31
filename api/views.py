from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items=Item.objects.all()
    serializer=ItemSerializer(items, many=True)
    print(serializer)
    return Response(serializer.data)
    #return Response(person)
    # person={'name':'subbu','age':'30'}
@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    