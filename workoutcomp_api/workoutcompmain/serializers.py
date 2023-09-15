from rest_framework import serializers
from workoutcompmain.models import Competition, Workout
from django.contrib.auth.models import User

class CompetitionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Competition
        fields = ['id', 'owner', 'users',
                  'name', 'startdate', 'enddate', 'ruleset', 'code']
        
class WorkoutSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Workout
        fields = ['id', 'owner',
                  'category', 'date', 'duration', 'intensity']

class UserSerializer(serializers.HyperlinkedModelSerializer):    
    competitions = CompetitionSerializer(many=True)
    workouts = WorkoutSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'competitions', 'workouts']