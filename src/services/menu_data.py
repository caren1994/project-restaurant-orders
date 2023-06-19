from models.ingredient import Ingredient
from models.dish import Dish
import pandas as pd


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        
        self.dishes = set()
        self.csv = pd.read_csv(source_path)

        dishes = dict()
        for file in self.csv.itertuples(index=False):
            name, price, ingredient, amount = file
            if name not in dishes:
                dish = Dish(name, price)
                dishes[name] = dish
                self.dishes.add(dish)

            ingredient = Ingredient(ingredient)
            dishes[name].add_ingredient_dependency(ingredient, amount)