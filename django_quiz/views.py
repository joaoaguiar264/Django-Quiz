from django.shortcuts import render, redirect
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

def add_survey(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        question = request.POST.get('question')
        option1 = request.FILES.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        option5 = request.POST.get('option5')

        Survey.objects.create(
            user_id=request.user.id,
            title = title,
            question = question,
            option1 = option1,
            option2 = option2,
            option3 = option3,
            option4 = option4,
            option5 = option5
        )
        return redirect('home')
    else:
        return render(request, 'pages/add-survey.html')