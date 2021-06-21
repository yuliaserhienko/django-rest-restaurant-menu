from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    ingredient = models.ManyToManyField(Ingredient, related_name='ingredients')
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name



