from django.shortcuts import render
from .models import Application, CategoryApplic
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

def index(request):
    num_applications = Application.objects.all().count()
    num_categoris = CategoryApplic.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request,'index.html', context={'num_applications': num_applications, 'num_categoris': num_categoris, 'num_visits':num_visits})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, template_name='register.html', context={'form': form})

class ProfilePage(generic.ListView):
        model = Application