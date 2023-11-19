from django.shortcuts import render

def contactHome(request):
    return render(request,'contact_ap/contact.html')

def gallaryView(request):
    return render(request,'contact_ap/gallary.html')

def tempareture(request):
    return render(request,'contact_ap/tempareture.html')
