from django.db import models
from django.contrib.auth.models import User

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
    code = models.TextField(unique=True)
    users = models.ManyToManyField('auth.User', blank=True)

class WorkOutCategories(models.IntegerChoices):
    Strength = 1,"Strength"
    Cardio = 2,"Cardio"
    Wellness = 3,"Wellness Activity"
    USP = 4,"USP"

class Workout(models.Model):
    category = models.IntegerField(choices=WorkOutCategories.choices)
    date = models.DateField()
    duration = models.IntegerField()
    intensity = models.IntegerField()
    note = models.TextField(blank=True, max_length=50)
    owner = models.ForeignKey('auth.User', related_name='workouts', on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.TextField(blank=True)
    restingheartrate = models.IntegerField(default=0)
    color = models.TextField(blank=True)

from django.db.models.signals import post_save

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)