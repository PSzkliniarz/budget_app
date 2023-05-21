from .models import Expense, Category
from .serializers import ExpenseSerializer, CategorySerializer
from rest_framework import mixins, viewsets


class ExpenseViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class CategoryViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
