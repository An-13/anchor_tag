from django.shortcuts import render

# Create your views here.
def Webtech(request):
    return render(request,'Webtech.html')

def Bootstrap(request):
    return render(request,'Bootstrap.html')