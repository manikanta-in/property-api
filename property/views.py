
from property.models import Property
from property.serializers import PropertySerializer
from rest_framework import viewsets
from rest_framework import permissions
from property.documents import PropertyDocument

from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    SUGGESTER_COMPLETION,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FilteringFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend,
)

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

class PropertySearchViewSet(DocumentViewSet):
    document = PropertyDocument
    serializer_class = PropertySerializer
    ordering = ('id',)
    lookup_field = 'id'
    queryset = Property.objects.all()

    filter_backends = [
        DefaultOrderingFilterBackend,
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
    ]

    search_fields = (
        'name',
        'description',
    )

    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'name': 'name',
    }

    suggester_fields = {
        'name_suggest': {
            'field': 'name.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }
