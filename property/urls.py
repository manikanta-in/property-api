from rest_framework import routers
from django.urls import include, path, re_path
from property import views 
#from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter()
router.register(r'list', views.PropertyViewSet)
router.register(r'search', views.PropertySearchViewSet, basename='properties')
#router.register(r'(?P<pk>[0-9]+)$', views.PropertyDetailsViewSet)
#schema_view = get_swagger_view(title='Snippets API')



urlpatterns = [ 
      #re_path(r'swagger', schema_view, name="docs"),
      path('', include(router.urls)),
      path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]