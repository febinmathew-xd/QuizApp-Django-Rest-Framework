# admin.py
from django.contrib import admin
from .models import Question, Option, Category

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4 # Set the number of options you want to add at once

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Category)

