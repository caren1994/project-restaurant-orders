from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    bife = Ingredient("bife")
    queijo = Ingredient("queijo mussarela")
    queijo2 = Ingredient("queijo mussarela")

    assert bife.name == "bife"
    assert queijo.name == "queijo mussarela"

    assert bife.__repr__() == "Ingredient('bife')"
    assert queijo.__repr__() == "Ingredient('queijo mussarela')"

    assert queijo == queijo2
    assert queijo != bife

    assert hash(bife) == hash("bife")
    assert hash(queijo) == hash("queijo mussarela")
    assert hash(bife) != hash(queijo)

    assert queijo.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,

    }
