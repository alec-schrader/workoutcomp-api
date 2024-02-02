from rest_framework import serializers
from workoutcompmain.models import Competition, Workout, Profile
from django.contrib.auth.models import User
        
class WorkoutSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Workout
        fields = ['id', 'owner',
                  'category', 'date', 'duration', 'intensity', 'note']

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ['id', 'user',
                  'username', 'restingheartrate', 'color']

class UserSerializer(serializers.HyperlinkedModelSerializer):    
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'profile']

    def update(self, instance, validated_data):
        profiledata = validated_data.get('profile', instance.profile)
        profile = ProfileSerializer(data=profiledata)
        if profile.is_valid():
            instance.profile.username = profile.data.get('username')
            instance.profile.color = profile.data.get('color')
            instance.profile.restingheartrate = profile.data.get('restingheartrate')
            instance.profile.save()
        return instance
    
class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields = ['id', 'users',
                  'name', 'startdate', 'enddate', 'ruleset', 'code']
