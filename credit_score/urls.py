from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('api/get_all_questions/', views.get_all_questions, name='get_all_questions'),
    path('save-answer/', views.save_answer, name='save_answer'),
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),
]
