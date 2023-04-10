from django.db import models
from django.contrib import admin
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    score = models.IntegerField()
    answer = models.CharField(max_length=200)

    @admin.display(
        boolean=True,
        ordering='score',
        description='Value',
    )
    
    def __str__(self):
        return self.question_text
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

class Users(models.Model):
    total_score = models.IntegerField(default=0)
    name = models.CharField(max_length=256, default="Nombre")
    latitude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)
        
    def __str__(self):
        return self.name
    
