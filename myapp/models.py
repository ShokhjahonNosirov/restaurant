from django.db import models
# Create your models here.


class Category(models.Model):
    class Meta:
        ordering = ["id"]
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Meal(models.Model):
    class Meta:
        ordering = ["id"]

    food = models.CharField(max_length=255, default="Plov", verbose_name="Food name")
    price = models.CharField(max_length=255, default="1 $")
    description = models.TextField(default="delicious")
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.food