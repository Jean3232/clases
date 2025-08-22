from django.http import HttpResponse

def inicio(request):
 nombre = "Jean camppos"
 return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre} !")
