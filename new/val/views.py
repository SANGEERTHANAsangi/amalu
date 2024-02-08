# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def a(request):
    return render(request,'b.html')
def b(request):
    return render(request,'a.html')
