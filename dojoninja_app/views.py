from django.shortcuts import render, redirect, HttpResponse
from .models import Dojos, Ninjas

# Create your views here.

def index(request):
    context = {
    "all_dojos": Dojos.objects.all(),
    
    }
    return render(request, 'index.html', context)  # dont forget to add context

# here are the function to get form data to save to the database.

def createdojo(request):
    Dojos.objects.create(name=request.POST["name"],city=request.POST["city"],state=request.POST['state'])
    return redirect("/")

def createninjas(request):
        this_dojo = Dojos.objects.all().get(id=request.POST["dojoname"])
        new_ninja = Ninjas.objects.create(first_name=request.POST["ninjafirstname"], last_name=request.POST["ninjalastname"], dojo=this_dojo)
        this_dojo.ninjas_owned.add(new_ninja)
        
        return redirect("/")