from django.urls import path
from .views import IslandDetail, IslandList

urlpatterns = [
    path('', IslandList.as_view(), name='island_list'),
    path('<int:pk>', IslandDetail.as_view(), name='island_detail')
]