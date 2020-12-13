from django.shortcuts import render

# Create your views here.

def index(request):
    # context = {
    # "all_the_dojos": Dojos.objects.all(),
    # "all_the_ninjas": Ninjas.objects.all()
    # }
    return render(request, 'index.html')  # dont forget to add context

def createdojo(request):
    if request.method == "POST":
        dojos = Dojos()
        dojos.name = request.Post.get("dojoname")  # be sure to add an input in the form with this matching name
        dojos.city = request.Post.get("cityname")  # be sure to add an input in the form with this matching name
        dojos.state = request.Post.get("statename")  # be sure to add an input in the form with this matching name

def createninjas(request):
    pass