from rest_framework import routers
from .api import CursoViewSet
router = routers.DefaultRouter()
router.register('api/curso', CursoViewSet, 'curso')
urlpatterns = router.urls