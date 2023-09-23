from workoutcompmain.models import Competition, Workout, Profile
from workoutcompmain.serializers import CompetitionSerializer, WorkoutSerializer, UserSerializer, ProfileSerializer
from auth.permissions import IsOwnerOrReadOnly, IsUserOrReadOnly
from rest_framework.permissions import  IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class CompetitionViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(users=[self.request.user])

    @action(methods=['get'], detail=False,
        url_path='code/(?P<code>\w+)')
    def getByCode(self, request, code):
        comp = get_object_or_404(Competition, code=code)
        data = CompetitionSerializer(comp, context={'request': request}).data
        return Response(data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True,
        url_path='workouts')
    def getWorkouts(self, request, pk):
        comp = Competition.objects.get(pk=pk)
        users = []
        for user in comp.users.all():
            users.append(user.id)

        workouts = Workout.objects.all().filter(date__lte=comp.enddate).filter(date__gte=comp.startdate).filter(owner__in=users).order_by('-id')

        data = WorkoutSerializer(workouts, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
    @action(methods=['get'], detail=True,
    url_path='users')
    def getUsers(self, request, pk):
        comp = Competition.objects.get(pk=pk)
        userids = []
        for user in comp.users.all():
            userids.append(user.id)

        users = User.objects.all().filter(id__in=userids)

        data = UserSerializer(users, many=True).data
        return Response(data, status=status.HTTP_200_OK)


    @action(detail=True, methods=['put'], url_path='addUser', url_name='addUser')
    def addUser(self, request, pk):
        print("test")
        user = self.request.user
        comp = Competition.objects.get(pk=pk)

        comp.users.add(user.id)
        comp.save()

        data = CompetitionSerializer(comp).data
        return Response(data, status=status.HTTP_200_OK)
    
    @action(methods=['get'], detail=False, url_path='userid/(?P<userid>\w+)')
    def getUserCompetitions(self, request, userid):
        competitions = Competition.objects.all().filter(users__id__exact=userid)
        data = CompetitionSerializer(competitions, many=True).data
        return Response(data, status=status.HTTP_200_OK)

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['get'], detail=False, url_path='userid/(?P<userid>\w+)')
    def getUserWorkout(self, request, userid):
        user = User.objects.all().get(pk=userid)
        workouts = Workout.objects.all().filter(owner__exact=user)
        data = WorkoutSerializer(workouts, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class UserViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = User.objects.all().select_related('profile')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserOrReadOnly]

    @action(methods=['get'], detail=False,
            url_path='username/(?P<username>\w+)')
    def getByUsername(self, request, username):
        user = get_object_or_404(User, username=username)
        data = UserSerializer(user, context={'request': request}).data
        return Response(data, status=status.HTTP_200_OK)
    
