from django.db import models

class RuleSets(models.IntegerChoices):
    Standard = 1, "Standard"
    Strength = 2,"Strength Focus"
    Cardio = 3,"Cardio Focus"
    Wellness = 4,"Wellness Focus"

class Competition(models.Model):
    name = models.TextField()
    startdate = models.DateField()
    enddate = models.DateField()
    ruleset = models.IntegerField(choices=RuleSets.choices, default=RuleSets.Standard)
    code = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='competitions', on_delete=models.CASCADE)
    users = models.ManyToManyField('auth.User')
    workouts = models.ManyToManyField('Workout')

class WorkOutCategories(models.IntegerChoices):
    Strength = 1,"Strength"
    Cardio = 2,"Cardio"
    Wellness = 3,"Wellness Activity"

class Workout(models.Model):
    category = models.IntegerField(choices=WorkOutCategories.choices)
    date = models.DateField()
    duration = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='workouts', on_delete=models.CASCADE)
