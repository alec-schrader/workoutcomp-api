from rest_framework import serializers
from workoutcompmain.models import Competition, Workout, Profile
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

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ['id', 'user',
                  'username', 'restingheartrate', 'color']

class UserSerializer(serializers.HyperlinkedModelSerializer):    
    competitions = CompetitionSerializer(many=True)
    workouts = WorkoutSerializer(many=True)
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'competitions', 'workouts', 'profile']

    def update(self, instance, validated_data):
        profiledata = validated_data.get('profile', instance.profile)
        profile = ProfileSerializer(data=profiledata)
        if profile.is_valid():
            instance.profile.username = profile.data.get('username')
            instance.profile.color = profile.data.get('color')
            instance.profile.restingheartrate = profile.data.get('restingheartrate')
            instance.profile.save()
        return instance