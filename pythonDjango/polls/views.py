from django.shortcuts import render
from .models import TeaVarity, Store
from django.shortcuts import get_object_or_404
from .forms import TeaVarityForm

# Create your views here.

def all_poll(request):
    teas = TeaVarity.objects.all()
    return render(request, 'polls/all_polls.html', {'teas' : teas})

def starapp(request):
    return render(request, 'polls/about_app.html')

def tea_detail(request, tea_id):
    tea = get_object_or_404(TeaVarity, pk=tea_id)
    return render(request, 'polls/tea_details.html', {'tea':tea})

def tea_store_view(request):
    stores = None
    if request.method == 'POST':
        form = TeaVarityForm(request.POST)
        if form.is_valid():
            tea_varity = form.cleaned_data['tea_varity']
            stores = Store.objects.filter(tea_varieties=tea_varity)
    else:
        form = TeaVarityForm()      
    return render(request, 'polls/tea_store.html' , {'stores': stores, 'form': form})
