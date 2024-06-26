import random

from praktikum.ingredient import Ingredient
from unittest.mock import Mock


class TestIngredient:
    mock_available_ingredients = Mock()
    mock_available_ingredients.return_value = [
        Ingredient('INGREDIENT_TYPE_SAUCE', 'spicy-x', 80),
        Ingredient('INGREDIENT_TYPE_SAUCE', 'space sauce', 10),
        Ingredient('INGREDIENT_TYPE_SAUCE', 'sweet and sour sauce', 30),
        Ingredient('INGREDIENT_TYPE_FILLING', 'beef meteorite', 300),
        Ingredient('INGREDIENT_TYPE_FILLING', 'beef vegan', 200),
        Ingredient('INGREDIENT_TYPE_FILLING', 'cutlet', 250)
    ]

    def test_ingredient_type(self):
        ingredient = random.choice(self.mock_available_ingredients())
        ingredient_type = ingredient.type
        get_type = ingredient.get_type()
        assert ingredient_type == get_type

    def test_ingredient_name(self):
        ingredient = random.choice(self.mock_available_ingredients())
        ingredient_name = ingredient.name
        get_name = ingredient.get_name()
        assert ingredient_name == get_name

    def test_ingredient_price(self):
        ingredient = random.choice(self.mock_available_ingredients())
        ingredient_price = ingredient.price
        get_price = ingredient.get_price()
        assert ingredient_price == get_price
