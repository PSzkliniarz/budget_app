from django.urls import path
from .views import AccountsView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('accounts/', AccountsView.as_view(), name='accounts_view'),

    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view())
]
