from rest_framework import serializers
from .models import Advert


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer for Advertisements"""

    class Meta:
        model = Advert
        fileds = '__all__'
