from django import forms
from .models import Question, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic', 'change']
        labels = {"change": "label for public"}

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'answear']

