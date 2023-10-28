from django.shortcuts import render

# Create your views here.

def home(request):
    # return HttpResponse('<h1> My Home Page</h1>')
    return render(request,'demoapp / place.html')