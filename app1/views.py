from django.shortcuts import render

# Create your views here.
def python(request):
    return render(request,'python.html')

def Django(request):
    return render(request,'Django.html')