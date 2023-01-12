from rest_framework import routers
from .api import UserStoriesViewSet

router = routers.DefaultRouter()

router.register('', UserStoriesViewSet, 'user_stories')

urlpatterns = router.urls