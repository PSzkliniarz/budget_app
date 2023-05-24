from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Expense, Category
from .serializers import ExpenseSerializer, CategorySerializer
from rest_framework import mixins, viewsets, generics


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = Expense.objects.filter(user=user)
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = Category.objects.filter(user=user)
        return queryset
