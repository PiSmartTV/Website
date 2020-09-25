from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    print("yay")
    return HttpResponse("<h1>Jej</h1>")