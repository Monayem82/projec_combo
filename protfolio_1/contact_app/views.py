from django.shortcuts import render
from contact_app.forms import contactUs

def contactHome(request):
    getform=contactUs(auto_id=False)
    getform.order_fields(field_order=['name','father_name','email','mobile','department','topic','describe'])
    templeteVariable={
        'foundform':getform,
    }
    return render(request,'contact_ap/contact.html',templeteVariable)

def gallaryView(request):
    return render(request,'contact_ap/gallary.html')

def tempareture(request):
    return render(request,'contact_ap/tempareture.html')
