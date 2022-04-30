from rest_framework import routers
from django.urls import include,path
from property import views 
 

router = routers.DefaultRouter()
router.register(r'list', views.PropertyViewSet)
router.register(r'search', views.PropertySearchViewSet, basename='properties')
#router.register(r'(?P<pk>[0-9]+)$', views.PropertyDetailsViewSet)

urlpatterns = [ 
      path('', include(router.urls)),
]