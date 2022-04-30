# documents.py

from django_opensearch_dsl import Document
from django_opensearch_dsl.registries import registry
from .models import Property


@registry.register_document
class PropertyDocument(Document):
    class Index:
        name = 'property'  # Name of the Opensearch index
        settings = {  # See Opensearch Indices API reference for available settings
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
        # Configure how the index should be refreshed after an update.
        # See Opensearch documentation for supported options.
        # This per-Document setting overrides settings.OPENSEARCH_DSL_AUTO_REFRESH.
        auto_refresh = False

    class Django:
        model = Property  # The model associated with this Document        
        fields = [  # The fields of the model you want to be indexed in Opensearch
            'location',
            'latittude',
            'longitude',
        ]
        # Paginate the django queryset used to populate the index with the specified size
        # This per-Document setting overrides settings.OPENSEARCH_DSL_QUERYSET_PAGINATION.
        queryset_pagination = 5000