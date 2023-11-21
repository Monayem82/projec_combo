from django.shortcuts import render
from django_1.models import DjangoTable,studentPublic
from django_1.forms import makePost,studentDetails

def homePage(request):
    return render(request,'django_1/dj1.html')

def dj(request):
    return render(request,'django_1/dj2.html')

def dataTable(request):
    data=DjangoTable.objects.all()
    student_list=studentPublic.objects.all()
    frm1=makePost(auto_id=True)
    frm2=studentDetails(auto_id=True,label_suffix=' = ')
    frm2.order_fields(field_order=['name','dep','roll'])
    variableList={  'tabledata' :data,
                    'sdata':student_list,
                    'form':frm1,
                    'form2':frm2,
                  }
    return render(request,'django_1/data.html',variableList)