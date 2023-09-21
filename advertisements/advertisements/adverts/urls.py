from django.urls import path

from adverts.views import AdvertisementListApiView

urlpatterns = [
    path('advert-list/', AdvertisementListApiView.as_view(), name='advert-list'),
    path('advert/<int:pk>/', AdvertisementListApiView.as_view(), name='advert'),
]
