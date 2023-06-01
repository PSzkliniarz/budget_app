from rest_framework import serializers
from . models import Expense, Category


class ExpenseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Expense
        fields = '__all__'

    #     extra_kwargs = {
    #         'user': {'read_only': True}
    #     }
    #
    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     if user.is_authenticated:
    #         validated_data['user'] = user
    #     return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
