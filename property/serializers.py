from django.contrib.auth.models import User, Group
from rest_framework import serializers
from property.models import Property


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ['name_of_owner', 'location', 'latittude', 'longitude',
                  'extent_in', 'road_size', 'village_locality', 'mandal', 'offer_price', 'near_market_value', 'distance_from_orr', 'contact_details', 'approch_road']
