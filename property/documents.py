# documents.py

from traceback import print_tb
from typing import Optional
from django_opensearch_dsl import Document, fields
from django_opensearch_dsl.registries import registry
from property.settings import PROPERT_SEARCH_IDX
from .models import Property
from django.db.models import QuerySet
from opensearch_dsl import Q

@registry.register_document
class PropertyDocument(Document):
    class Index:
        name = PROPERT_SEARCH_IDX  # Name of the Opensearch index
        settings = {  # See Opensearch Indices API reference for available settings
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
        # Configure how the index should be refreshed after an update.
        # See Opensearch documentation for supported options.
        # This per-Document setting overrides settings.OPENSEARCH_DSL_AUTO_REFRESH.
        auto_refresh = True

    class Django:
        model = Property  # The model associated with this Document        
        fields = [  # The fields of the model you want to be indexed in Opensearch
            'name_of_owner',
            'location',
            'latittude',
            'longitude',
            'near_market_value',
            'offer_price',
            'contact_details'
        ]

    
        # Paginate the django queryset used to populate the index with the specified size
        # This per-Document setting overrides settings.OPENSEARCH_DSL_QUERYSET_PAGINATION.
        queryset_pagination = 5000

    #location = fields.KeywordField()