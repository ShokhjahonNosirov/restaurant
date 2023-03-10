from rest_framework import generics
from rest_framework.response import Response
from .models import Meal, Category
from .serializers import MealSerializer, CategorySerializer, Cat_meal_Serializer
from rest_framework.views import APIView


class Meals(generics.ListAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

class Category(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CatItem(APIView):
    def get(self, request, format=None, **kwargs):
        category = Meal.objects.filter(category__name=kwargs['cat_name'])
        serializer = Cat_meal_Serializer(category, many=True)
        return Response(serializer.data)