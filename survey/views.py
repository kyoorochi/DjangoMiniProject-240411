from django.shortcuts import render, redirect
from .models import Survey, Question, Answer
from django.core.paginator import Paginator

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age_group = request.POST.get('age_group')
        Survey.objects.create(name=name, gender=gender, age_group=age_group)
        return redirect('question')
    return render(request, 'home.html')

def question_view(request):
    page = request.GET.get('page', '1')  
    questions = Question.objects.filter(is_active=True)
    paginator = Paginator(questions, 1)  
    questions = paginator.get_page(page)
    
    return render(request, 'question.html', {'questions': questions})

def answer_view(request):
    if request.method == 'POST':
        yes = request.POST.get('yes')
        no = request.POST.get('no')        
        Answer.objects.create(yes=yes, no=no)
        return redirect('result')
    return render(request, 'question.html')