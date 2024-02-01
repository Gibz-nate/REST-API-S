from django.http import JsonResponse
from .models import taifa
from .serializers import taifaserials
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])


def taifa_list(request):


    if request.method == 'GET':

        nations = taifa.objects.all()
        serialed = taifaserials(nations, many=True)
        return JsonResponse({'taifa':serialed.data})
    if request.method == 'POST':
        serialed = taifaserials(data=request.data)
        if serialed.is_valid():
            serializer.save()
            return Response(serialed.data, status=status.HTTP_201_CREATED)



@api_view(['GET','PUT','DELETE'])            
def taifa_detail(request, id):

    try:
        taifa = taifa.objects.get(pk=id)
    except  taifa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   

    if request.method == 'GET':
        serializer = taifaserials(taifa)
        return Response(serializer.data)

        
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass




