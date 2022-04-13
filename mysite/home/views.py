from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    university="Samdu"
    dept = "Raqamli texnologiyalar"
    context = {
        'university': university,
        'department': dept,
    }
    return render(request, 'index.html',context)
