from django.shortcuts import render
from .models import Survey
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')

def index(request):
    surveys = Survey.objects.all()
    return render(request, 'pages/index.html', {'surveys':surveys})

def search_survey(request):
    q = request.GET.get('q')
    surveys = Survey.objects.filter(name__icontains=q)
    return render(request, 'pages/index.html', {'surveys':surveys})
