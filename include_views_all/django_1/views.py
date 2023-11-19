from django.shortcuts import render

def homePage(request):
    return render(request,'django_1/dj1.html')

def dj(request):
    return render(request,'django_1/dj2.html')