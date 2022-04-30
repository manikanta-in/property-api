from django.contrib.auth.models import User, Group
from rest_framework import serializers
from property.models import Property


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ['location', 'latittude','longitude']


