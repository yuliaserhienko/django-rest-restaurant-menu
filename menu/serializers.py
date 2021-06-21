from rest_framework import serializers
from .models import Category, Dish, Ingredient


class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = ['id', 'name', 'category', 'ingredient']


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    dishes = DishSerializer(source='categories', many=True, required=False, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'dishes')


class MenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(source='categories', many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'dishes')

