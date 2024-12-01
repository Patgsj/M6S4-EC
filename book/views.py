from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenidos a la app book")

# Create your views here.
