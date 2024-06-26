import pytest

from praktikum.burger import Burger
from praktikum.database import *


@pytest.fixture
def burger(bun):
    burger = Burger()
    burger.set_buns(bun)
    return burger


@pytest.fixture
def bun():
    return Bun('white bun', 200)


@pytest.fixture
def sauce_ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, 'sour cream', 200)


@pytest.fixture
def filling_ingredient():
    return Ingredient(INGREDIENT_TYPE_FILLING, 'sausage', 300)
