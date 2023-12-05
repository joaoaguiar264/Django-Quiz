from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
    title = models.CharField(max_length=256)
    question = models.CharField(max_length=256)

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Survey'
        verbose_name_plural = 'Surveys'
