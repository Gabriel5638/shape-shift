from django.contrib import admin
from .models import Question, Answer
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Answer)