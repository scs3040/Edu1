from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']

    # fieldsets = [
    #     ('Qustion Statement', {'fields': ['question_text']}),
    #     ('Date Information', {'fields': ['pub_date']})
    # ]

    fieldsets = [
        ('Qustion Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin )
admin.site.register(Choice)