
from property.models import Property
from property.serializers import PropertySerializer
from rest_framework import viewsets
from rest_framework import permissions
from property.documents import PropertyDocument


from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

class PropertyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]


class PropertyDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]

class PropertySearchViewSet(viewsets.ModelViewSet):
    document = PropertyDocument
    serializer_class = PropertySerializer
    queryset = PropertyDocument.search()
    permission_classes = [permissions.IsAuthenticated]

