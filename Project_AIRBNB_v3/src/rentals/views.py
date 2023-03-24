from django.shortcuts import render
from .models import Listings

# Create your views here.

def objet(request):
    objs = Listings.objects.all()
    context = {'objs': objs}

    return render(request, "rentals/index.html", context)

    # def __str__(self):
    #     return self.title
