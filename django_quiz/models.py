from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    is_open = models.BooleanField(default=True)
    
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    option5 = models.CharField(max_length=255)
    
    option1_results = models.IntegerField(default=0)
    option2_results = models.IntegerField(default=0)
    option3_results = models.IntegerField(default=0)
    option4_results = models.IntegerField(default=0)
    option5_results = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Survey'
        verbose_name_plural = 'Surveys'
