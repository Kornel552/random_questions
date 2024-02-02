from django.db import models
from ckeditor.fields import RichTextField

class Topic(models.Model):
    topic = models.CharField(max_length=300)

    def __str__(self):
        return str(self.topic)

class Question(models.Model):
    key = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answear = RichTextField(config_name='default')
