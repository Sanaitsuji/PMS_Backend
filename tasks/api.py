from .models import Task
from rest_framework import viewsets, permissions
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer

    def get_queryset(self):
        query_set = self.queryset
        user_story = self.request.query_params.get('user_story')
        if user_story:
            query_set = query_set.filter(user_story=user_story)
            return query_set
        else:
            query_set = Task.objects.all()
            return query_set