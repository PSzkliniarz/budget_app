from django.urls import path
from .views import ExpenseView, CategoryView

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view())
    path('expenses/', ExpenseView.as_view(), name='accounts_view'),
    path('categories/', CategoryView.as_view(), name='accounts_view'),
]
