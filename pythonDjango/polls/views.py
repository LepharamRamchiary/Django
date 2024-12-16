from django.shortcuts import render
from .models import TeaVarity
from django.shortcuts import get_object_or_404

# Create your views here.

def all_poll(request):
    teas = TeaVarity.objects.all()
    return render(request, 'polls/all_polls.html', {'teas' : teas})

def starapp(request):
    return render(request, 'polls/about_app.html')

def tea_detail(request, tea_id):
    tea = get_object_or_404(TeaVarity, pk=tea_id)
    return render(request, 'polls/tea_details.html', {'tea':tea})
