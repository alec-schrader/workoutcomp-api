# Generated by Django 4.2.4 on 2023-09-03 23:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workoutcompmain', '0002_competitionuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CompetitionUser',
        ),
    ]
