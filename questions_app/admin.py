from django.contrib import admin
from .models import Topic, Question

class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic',)
admin.site.register(Topic, TopicAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('key', 'question', 'answear')
admin.site.register(Question, QuestionAdmin)