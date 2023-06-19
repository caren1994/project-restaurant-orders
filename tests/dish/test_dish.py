from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    lasanha_queijo = Dish("lasanha queijo", 25.00)
    muqueca_camarao = Dish('muqueca_camarao', 35.00)
    lasanha_queijo.add_ingredient_dependency(Ingredient('queijo mussarela'), 5)

    assert lasanha_queijo.name == 'lasanha queijo'
    assert lasanha_queijo == lasanha_queijo
    assert hash(lasanha_queijo) == hash(lasanha_queijo)
    assert hash(lasanha_queijo) != hash(muqueca_camarao)
    assert repr(lasanha_queijo) == "Dish('lasanha queijo', R$25.00)"
    assert lasanha_queijo.get_ingredients() == {Ingredient('queijo mussarela')}
    assert lasanha_queijo.get_restrictions() == {
        Restriction.ANIMAL_DERIVED, Restriction.LACTOSE
        }

    with pytest.raises(TypeError):
        Dish('name', 'price')
    with pytest.raises(ValueError):
        Dish('name', 0)
