from .models import Technology, CharacterHated, CharacterLoved, UnimpressiveSections
from rest_framework import viewsets, permissions
from .serializers import TechnologySerializer, CharacterHatedSerializer, CharacterLovedSerializer, UnimpressiveSectionsSerializer

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TechnologySerializer

class CharacterHatedViewSet(viewsets.ModelViewSet):
    queryset = CharacterHated.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CharacterHatedSerializer

class CharacterLovedViewSet(viewsets.ModelViewSet):
    queryset = CharacterLoved.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CharacterLovedSerializer

class UnimpressiveSectionsViewSet(viewsets.ModelViewSet):
    queryset = UnimpressiveSections.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UnimpressiveSectionsSerializer
