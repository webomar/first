from django.contrib import admin

# Register your models here.
from .models import Question, rClass,Choice
admin.site.register(Question)
admin.site.register(rClass)
admin.site.register(Choice)
