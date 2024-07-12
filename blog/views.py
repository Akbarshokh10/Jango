from django.shortcuts import render
from .models import Card,About
# Create your views here.


def index(request):
    cards = Card.objects.all()
    return render(request,'index.html',{'cards':cards})

def about(request):
    abouts = About.objects.all()
    return render(request,'about.html',{'abouts':abouts})