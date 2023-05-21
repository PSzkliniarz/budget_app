from rest_framework.response import Response
from rest_framework import generics
from .models import Expense, Category
from .serializers import ExpenseSerializer, CategorySerializer


class ExpenseView(generics.RetrieveAPIView):
    queryset = Expense.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ExpenseSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryView(generics.RetrieveAPIView):
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
