class TestBurger:

    def test_add_ingredient(self, burger, sauce_ingredient, filling_ingredient):
        burger.add_ingredient(filling_ingredient)
        assert len(burger.ingredients) == 1
        burger.add_ingredient(sauce_ingredient)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].name == "sausage"
        assert burger.ingredients[1].price == 200

    def test_remove_ingredient_list(self, burger, sauce_ingredient):
        burger.add_ingredient(sauce_ingredient)
        assert len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, sauce_ingredient, filling_ingredient):
        burger.add_ingredient(sauce_ingredient)
        burger.add_ingredient(filling_ingredient)
        assert burger.ingredients[0].name == "sour cream"
        assert burger.ingredients[1].name == "sausage"
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].name == "sausage"
        assert burger.ingredients[1].name == "sour cream"

    def test_get_price_returns_expected_price(self, bun, burger):
        bun_price = burger.bun.get_price() * 2
        assert burger.get_price() == bun_price

    def test_get_receipt_returns_expected_receipt(self, burger):
        receipt = burger.get_receipt()
        assert '(==== white bun ====)' in receipt
