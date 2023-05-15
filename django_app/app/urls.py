from django.urls import path
from .views import ExpenseView, CategoryView

urlpatterns = [
    path('expenses/', ExpenseView.as_view(), name='accounts_view'),
    path('categories/', CategoryView.as_view(), name='accounts_view'),
]
