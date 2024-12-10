from django.shortcuts import render

# Create your views here.

def all_poll(request):
    return render(request, 'polls/all_polls.html')

def starapp(request):
    return render(request, 'polls/about_app.html')
