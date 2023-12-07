from django.shortcuts import render, redirect
from .models import Survey
from datetime import datetime
from .utils import send_email
from django.contrib.auth.decorators import login_required


def index(request):
    surveys = Survey.objects.all()
    return render(request, 'pages/index.html', {'surveys':surveys})


def search_survey(request):
    q = request.GET.get('q')
    surveys = Survey.objects.filter(name__icontains=q)
    return render(request, 'pages/index.html', {'surveys':surveys})

@login_required(redirect_field_name='login')

def add_survey(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        question = request.POST.get('question')
        option1 = request.POST.get('option1')
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

def close_survey(request, id):
    survey = Survey.objects.get(id=id)
    survey.is_open = False
    survey.save()
    survey_respondents = survey.respondents.all()
    for user in survey_respondents:
        send_email("The Survey is Closed", f"The survey \"{survey.title}\" is closed\nRESULTS\n{survey.option1} - {survey.option1_results} Votes\n{survey.option2} - {survey.option2_results} Votes\n{survey.option3} - {survey.option3_results} Votes\n{survey.option4} - {survey.option4_results} Votes\n{survey.option5} - {survey.option5_results} Votes\n\n{datetime.now()}", user.email)

    return redirect('my_surveys')
    

def survey_details(request, id):
    survey = Survey.objects.get(id=id)
    return render(request, 'pages/survey-details.html', {'survey':survey})

def my_surveys(request):
    surveys = Survey.objects.filter(user_id=request.user.id)
    return render(request, 'pages/my-surveys.html', {'surveys':surveys})

@login_required(redirect_field_name='login')

def answer_survey(request, id):
    survey = Survey.objects.get(id=id)
    if request.method == 'POST':
        option1_result = request.POST.get('option1_results')
        option2_result = request.POST.get('option2_results')
        option3_result = request.POST.get('option3_results')
        option4_result = request.POST.get('option4_results')
        option5_result = request.POST.get('option5_results')

        if request.user not in survey.respondents.all():
            survey.respondents.add(request.user)

        if option1_result != None:
            survey.option1_results += int(option1_result)
        
        if option2_result != None:
            survey.option2_results += int(option2_result)

        if option3_result != None:
            survey.option3_results += int(option3_result)

        if option4_result != None:
            survey.option4_results += int(option4_result)

        if option5_result != None:
            survey.option5_results += int(option5_result)
    survey.save()
    return redirect('home')
