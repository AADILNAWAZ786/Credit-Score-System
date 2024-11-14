from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Question, Option, UserResponse, UserScore, QuizResult
from django.shortcuts import get_object_or_404
import logging

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'credit_score/home.html')

@login_required(login_url='/accounts/login/')
def quiz(request):
    # Fetch all questions and options
    questions = Question.objects.all()
    question_data = [
        {"text": question.text, "options": [{"text": opt.text, "score": opt.score_value} for opt in question.options.all()]}
        for question in questions
    ]
    return render(request, 'credit_score/quiz.html', {'questions': question_data})

@csrf_exempt
@login_required(login_url='/accounts/login/')
def get_all_questions(request):
    questions = Question.objects.all()
    all_questions = []

    for question in questions:
        options = Option.objects.filter(question=question)
        question_data = {
            'id': question.id,
            'text': question.text,
            'options': [
                {'id': option.id, 'text': option.text, 'score': option.score_value} 
                for option in options
            ]
        }
        all_questions.append(question_data)

    return JsonResponse({'questions': all_questions})

logger = logging.getLogger(__name__)
@csrf_exempt
@login_required(login_url='/accounts/login/')
def save_answer(request):
    if request.method == 'POST':
        try:
            question_id = request.POST.get('question_id')
            selected_option_id = request.POST.get('selected_option')

            if not question_id or not selected_option_id:
                return JsonResponse({'status': 'error', 'message': 'Missing data'})

            question = get_object_or_404(Question, id=question_id) 
            selected_option = get_object_or_404(Option, id=selected_option_id)  

            score = selected_option.score_value

            if 'score' not in request.session:
                request.session['score'] = 0

            request.session['score'] += score
            request.session.modified = True  

            return JsonResponse({'status': 'success', 'score': request.session['score']})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


@login_required(login_url='/accounts/login/')
def submit_quiz(request):
    score = request.session.get('score', 0) 
    return render(request, 'credit_score/result.html', {'score': score}) 
