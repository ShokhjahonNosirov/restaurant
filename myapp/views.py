
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from .models import Meal, Category
from .serializers import MealSerializer, CategorySerializer, Cat_meal_Serializer
from rest_framework.views import APIView


class Meals(ListAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()
    print(queryset)


class Category(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    print(queryset)


class CatItem(ListAPIView):
    serializer_class = Cat_meal_Serializer
    def get_queryset(self):
        queryset = Meal.objects.filter(category__name=self.kwargs["cat_name"])
        print(queryset)
        return queryset



class ItemDetail(RetrieveAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

