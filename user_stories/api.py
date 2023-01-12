from .models import UserStories
from rest_framework import viewsets, permissions
from .serializers import UserStoriesSerializer

class UserStoriesViewSet(viewsets.ModelViewSet):
    queryset = UserStories.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserStoriesSerializer

    def get_queryset(self):
        query_set = self.queryset
        project = self.request.query_params.get('project')
        if project:
            query_set = query_set.filter(project=project)
            return query_set
        else:
            query_set = UserStories.objects.all()
            return query_set