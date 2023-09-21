from rest_framework import generics
from rest_framework.response import Response

from .models import Advert
from .serializers import AdvertisementSerializer


class AdvertisementListApiView(generics.ListAPIView, generics.RetrieveAPIView):
    """Class for getting of advertisements"""

    serializer_class = AdvertisementSerializer
    queryset = Advert.objects.all().select_related('category', 'city')

    def get(self, request, *args, **kwargs):
        if not kwargs.get('pk'):
            return super().list(self, request, *args, **kwargs)
        obj = super().get_object()
        obj.views += 1
        obj.save()
        serializer = self.serializer_class(obj)
        return Response(serializer.data)
