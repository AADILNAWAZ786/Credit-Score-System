from django.core.management.base import BaseCommand
from credit_score.models import Question, Option

class Command(BaseCommand):
    help = 'Populate questions and options for the quiz'

    def handle(self, *args, **kwargs):
        # Define the questions and options
        questions = [
            {
                "text": "Do you have a business plan?",
                "options": [("Yes", 10), ("No", 0), ("Working on it", 5)]
            },
            {
                "text": "Have you registered your business?",
                "options": [("Yes", 10), ("No", 0), ("Planning to", 5)]
            },
            {
                "text": "Do you have a business website?",
                "options": [("Yes", 10), ("No", 0), ("In progress", 5)]
            },
            {
                "text": "Have you identified your target market?",
                "options": [("Yes", 10), ("No", 0), ("Partially", 5)]
            },
            {
                "text": "Do you have a marketing strategy?",
                "options": [("Yes", 10), ("No", 0), ("In development", 5)]
            },
            {
                "text": "Have you secured funding for your business?",
                "options": [("Yes", 10), ("No", 0), ("In process", 5)]
            },
            {
                "text": "Do you have a business mentor or advisor?",
                "options": [("Yes", 10), ("No", 0), ("Looking for one", 5)]
            },
            {
                "text": "Do you have a dedicated workspace?",
                "options": [("Yes", 10), ("No", 0), ("Working on it", 5)]
            },
            {
                "text": "Have you set your business goals?",
                "options": [("Yes", 10), ("No", 0), ("Partially", 5)]
            },
            {
                "text": "Do you have an accounting system in place?",
                "options": [("Yes", 10), ("No", 0), ("Setting it up", 5)]
            },
            {
                "text": "Have you established a business network?",
                "options": [("Yes", 10), ("No", 0), ("In progress", 5)]
            },
            {
                "text": "Do you have a customer service plan?",
                "options": [("Yes", 10), ("No", 0), ("Developing it", 5)]
            },
        ]

        # Populate the questions and options in the database
        for q in questions:
            question = Question.objects.create(text=q['text'])
            for option_text, score in q['options']:
                Option.objects.create(question=question, text=option_text, score_value=score)

        self.stdout.write(self.style.SUCCESS('Questions and options populated successfully!'))
