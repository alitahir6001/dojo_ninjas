from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')  # dont forget to add context