from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'nlp', views.NlpViewSet)

from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]