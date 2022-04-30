
from property.models import Property
from property.serializers import PropertySerializer
from rest_framework import viewsets
from rest_framework import permissions
from property.documents import PropertyDocument


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
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        location = self.request.query_params.get('location')
        print(location)
        if location != None : 
            query = {'location': location}
            return PropertyDocument.search().query('term', **query)
        return PropertyDocument.search()
