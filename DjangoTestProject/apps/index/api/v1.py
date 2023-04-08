from django.http import JsonResponse, HttpResponse

from django.core import serializers


def player(request):
    if request.method == "GET":
        #print(type(Player.objects.get(name="Tom")))
        return HttpResponse('OK')
        #return HttpResponse(serializers.serialize('json', Player.objects.filter(name="Tom")))
    else:
        return JsonResponse({"error": 'BadRequest', 'code': '401'})