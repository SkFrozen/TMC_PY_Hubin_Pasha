class PizzaBuilder():

    def __init__(self):
        self.reset()

    def reset(self):
        self._pizza = Pizza()

    @property
    def pizza(self):
        pizza = self._pizza
        self.reset()
        return pizza
    
    def add_pepperoni(self):
        self._pizza.add_ingredient("pepperoni")

    def add_bacon(self):
        self._pizza.add_ingredient("bacon")

    def add_cheese(self):
        self._pizza.add_ingredient("cheese")

    def add_mushrooms(self):
        self._pizza.add_ingredient("mushrooms")

    def add_onions(self):
        self._pizza.add_ingredient("onions")

    def add_size(self, size):
        self._pizza.add_ingredient(size)


class Pizza:

    def __init__(self):
        self.ingredients = list()

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def list_ingredients(self):
        print(f"Ingredients: {", ".join(self.ingredients[1:])} \
            \nSize: {self.ingredients[0]}")


class PizzaDirector:

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def make_pizza(self, size):
        self._builder.add_size(size)
        self._builder.add_pepperoni()
        self._builder.add_cheese()
        self._builder.pizza.list_ingredients()

    def make_big_pizza(self, size):
        self._builder.add_size(size)
        self._builder.add_pepperoni()
        self._builder.add_mushrooms()
        self._builder.add_onions()
        self._builder.add_cheese()
        self._builder.pizza.list_ingredients()


builder = PizzaBuilder()
director = PizzaDirector()
director.builder = builder

director.make_pizza("36sm")
director.make_big_pizza("52sm")
