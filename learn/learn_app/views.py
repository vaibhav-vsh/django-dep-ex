from django.shortcuts import render
from django.http import HttpResponse
from learn_app.models import Kid,Student

# Create your views here.

def index(request):
    return HttpResponse("This is the views.py file in the learn_app! Base func!")

def index1(request):
    return HttpResponse("This is the views.py file in the learn_app! Index1 func!")

def index2(request):
    return HttpResponse("This is the views.py file in the learn_app! Index2 func!")

def temps(request):
    my_dict={
    'print_me':'This is coming from views.py via template tag!',
    'and_me':'This is also coming from views.py via template tag! Second key!'
    }
    return render(request,'learn_app/index.html',context=my_dict)

def temps2(request):
    return render(request,'learn_app/index2.html')

def data(request):
    kid_list=Kid.objects.all()
    stu_list=Student.objects.all()
    sch_dict={'kids':kid_list,'stu':stu_list}
    return render(request,'learn_app/data.html',context=sch_dict)
