# Generated by Django 4.2.4 on 2023-09-22 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workoutcompmain', '0006_alter_competition_code_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='color',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='restingheartrate',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.TextField(blank=True),
        ),
    ]
