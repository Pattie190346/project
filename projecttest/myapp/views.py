from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def index(request):
    name = "PATTIE"
    age = 20
    return render(request,"index.html",{"name":name,"age":age})

def about(request):
    dt = date.today()
    date = {
        'colors' : ['red','green','blue'],
        'flowers' : {'a':'กุหลาบ','b':'มะลิ','c':'กล้วยไม้'},
        'date' : dt #อ๊อบเจ็ก
    }
    return render(request,"about.html")

def gallery(request):
    return render(request,"gallery.html")