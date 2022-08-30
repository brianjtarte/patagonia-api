from django.urls import path
from .views import CampsiteList, CampsiteDetail

urlpatterns = [
    path('', CampsiteList.as_view(), name='campsite_list'),
    path('<int:pk>', CampsiteDetail.as_view(), name='campsite_detail')
]