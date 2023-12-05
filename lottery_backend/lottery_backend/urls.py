from django.urls import path, include
from rest_framework import routers
from .views import PerformanceViewSet, WinnerViewSet, LotteryEntryViewSet

router = routers.DefaultRouter()
router.register(r'performances', PerformanceViewSet, basename='performance')

urlpatterns = [
    path('', include(router.urls)),
    path('winners/select', WinnerViewSet.as_view({'post': 'create'}), name='winner-create'),
    path('winners', WinnerViewSet.as_view({'get': 'list'}), name='winner-list'),
    path('lottery_entries', LotteryEntryViewSet.as_view({'post': 'create', 'get': 'list'}), name='lottery_entry-list')
]