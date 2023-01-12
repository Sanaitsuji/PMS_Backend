from rest_framework import routers
from .api import TechnologyViewSet, CharacterHatedViewSet, CharacterLovedViewSet, UnimpressiveSectionsViewSet

router = routers.DefaultRouter()

router.register('technology', TechnologyViewSet, 'technology')
router.register('character_hated', CharacterHatedViewSet, 'character_hated')
router.register('character_loved', CharacterLovedViewSet, 'character_loved')
router.register('unimpressive_sections', UnimpressiveSectionsViewSet, 'unimpressive_sections')

urlpatterns = router.urls