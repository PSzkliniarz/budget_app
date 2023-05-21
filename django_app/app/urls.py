from django.urls import path
from .views import ExpenseViewSet, CategoryViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('expense/', ExpenseViewSet.as_view({'get': 'list', 'post': 'create'}), name='expense-list'),
    path('expense/<int:pk>/', ExpenseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='expense-detail'),
    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category-detail'),

    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
]
