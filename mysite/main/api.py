from main.models import Tutorial
from rest_framework import viewsets, permissions
from .serializers import TutorialSerializer

#Tutorial Viewset

class TutorialViewset(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TutorialSerializer