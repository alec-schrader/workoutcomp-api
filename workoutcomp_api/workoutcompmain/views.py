from workoutcompmain.models import Competition, Workout
from workoutcompmain.serializers import CompetitionSerializer, WorkoutSerializer, UserSerializer
from auth.permissions import IsOwnerOrReadOnly, HasAdminPermission
from rest_framework.permissions import  IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, users=[self.request.user])

    @action(detail=True, methods=['put'], url_path='addUser/(?P<username>\w+)', url_name='addUser')
    def addUser(self, request, pk, username):
        user = get_object_or_404(User, username=username)

        comp = Competition.objects.get(pk=pk)

        comp.users.add(user.id)
        comp.save()

        data = CompetitionSerializer(comp).data
        return Response(data, status=status.HTTP_200_OK)

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    @action(methods=['get'], detail=False,
            url_path='username/(?P<username>\w+)')
    def getByUsername(self, request, username):
        user = get_object_or_404(User, username=username)
        data = UserSerializer(user, context={'request': request}).data
        return Response(data, status=status.HTTP_200_OK)
