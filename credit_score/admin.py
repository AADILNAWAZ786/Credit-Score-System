
from django.contrib import admin
from .models import Question, Option, UserResponse, UserScore

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserResponse)
admin.site.register(UserScore)
