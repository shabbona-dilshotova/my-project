from django.shortcuts import render
from .models import Index

def index(request):
    salom = Index.objects.all()

    context = {
        'index': salom
    }
    return render (request, 'index.html', context)# Create your views here.
