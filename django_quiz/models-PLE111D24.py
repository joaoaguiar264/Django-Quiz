from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Survey'
        verbose_name_plural = 'Surveys'
