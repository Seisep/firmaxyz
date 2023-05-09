from django.shortcuts import render

# Create your views here.

def hello(request):
    name = "Patrick Seise"
    context = {
        'name' : name
    }
    return render(request, 'app1/hello.html', context)

def seite2(request):
    return render(request, 'app1/hello2.html', context)