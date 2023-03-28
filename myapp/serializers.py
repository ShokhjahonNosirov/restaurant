from rest_framework import serializers
from .models import Meal, Category


class MealSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    class Meta:
        model = Meal
        fields = [
            'id', 'food', 'price', 'ogirlik', 'bolaklar_soni', 'sostav', 'description', 'discount', 'category_name'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
        ]

class Cat_meal_Serializer(MealSerializer):
#    category = CategorySerializer(read_only=True)

    class Meta:
        model = Meal
        fields = [
            'id', 'category_name', 'food', 'price', 'ogirlik', 'bolaklar_soni', 'sostav', 'discount', 'description'
        ]
