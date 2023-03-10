from django.urls import path
from .views import Meals, Category, CatItem

app_name = 'myapp'

urlpatterns = [
    path('', Meals.as_view(), name='myapp'),
    path('category', Category.as_view(), name='category'),
    path('<str:cat_name>/', CatItem.as_view(), name='category')
    # path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
    # path('q/<str:topic>/', QuizQuestion.as_view(), name='questions'),
]



