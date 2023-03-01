from rest_framework import serializers
from .models import Meal, Category


class MealSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Meal
        fields = [
            'food', 'price', 'description', 'category_name'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
