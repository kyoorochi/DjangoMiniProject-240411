from django.shortcuts import render, redirect
from .models import Survey

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age_group = request.POST.get('age_group')
        Survey.objects.create(name=name, gender=gender, age_group=age_group)
        return redirect('home')
    return render(request, 'home.html')