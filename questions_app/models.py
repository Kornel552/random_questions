from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Topic(models.Model):
    topic = models.CharField(max_length=300)
    change = models.BooleanField(default=True)

    def __str__(self):
        return str(self.topic)

class Question(models.Model):
    key = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answear = CKEditor5Field(config_name='default')
