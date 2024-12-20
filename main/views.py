from rest_framework import viewsets
from .models import SpyCat, Mission, Target
from .serializers import SpyCatSerializer, MissionSerializer, TargetSerializer, MissionWithTargetsSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    @action(detail=False, methods=['post'])
    def create_with_targets(self, request):
        serializer = MissionWithTargetsSerializer(data=request.data)
        if serializer.is_valid():
            mission = serializer.save()
            return Response({'message': 'Mission and targets created successfully', 'mission_id': mission.id}, status=201)
        return Response(serializer.errors, status=400)


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
