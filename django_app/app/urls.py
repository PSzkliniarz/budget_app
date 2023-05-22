from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ExpenseViewSet, CategoryViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'expense', ExpenseViewSet, basename='expense')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    *router.urls,

    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
]
