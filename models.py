from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms


class Quest(models.Model):
    question=models.TextField()
    a=models.TextField()
    aw=models.PositiveIntegerField()
    b=models.TextField()
    bw=models.PositiveIntegerField()
    c=models.TextField()
    cw=models.PositiveIntegerField()
    d=models.TextField()
    dw=models.PositiveIntegerField()
    domain=models.CharField(
        max_length=2,
        choices=[
            ('co', 'Confidence'),
            ('fi', 'Fitness'),
            ('ac', 'Acadamics'),
            ('pd', 'Personality Development'),
            ('mi', 'Miscellenous')
        ],
        default='mi',
    )
    def __str__ (self):
        return self.question+ " Options are: 1."+self.a+" 2. "+self.b+" 3. "+self.c+" 4. "+self.d

class Attempt(models.Model):
    attempter=models.ForeignKey(User,on_delete=models.CASCADE)
    confidence_attempt=models.BooleanField()
    confidence_score=models.IntegerField()
    academics_attempt=models.BooleanField()
    academics_score=models.IntegerField()
    fitness_attempt=models.BooleanField()
    fitness_score=models.IntegerField()
    personality_attempt=models.BooleanField()
    personality_score=models.IntegerField()

    def __str__(self):
        return self.attempter+' '+str(self.confidence_score)+' '+str(self.academics_score)+' '+str(self.fitness_score)+' '+str(self.personality_score)
  

    