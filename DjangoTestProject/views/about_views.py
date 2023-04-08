from django.http import HttpResponse

def main(request):
    return HttpResponse("О сайте")

def contact(request):
    return HttpResponse("Контакты")