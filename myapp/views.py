from rest_framework import generics
from rest_framework.response import Response
from .models import Meal, Category
from .serializers import MealSerializer, CategorySerializer
from rest_framework.views import APIView


class Meal(generics.ListAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

class Category(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()