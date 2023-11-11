from django.http import JsonResponse
from .serializers import taifaserials

def taifa_list(request):
    nations = taifa.objects.all()
    serialed = taifaserials(nations, many=True)
    return JsonResponse(serialed.data)
