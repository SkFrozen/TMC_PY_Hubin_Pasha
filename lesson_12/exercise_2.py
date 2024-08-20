class BeeElephant:

    def __init__(self, bee: int, elephant: int):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        return True if self.bee >= self.elephant else False

    def trumpet(self):
        return "tu-tu-doo-doo" if self.elephant >= self.bee else "wzzzzzz"

    def eat(self, meal: str, value: int):
        if meal == "nectar":
            self.elephant = 0 if self.elephant - value < 0 else self.elephant - value
            self.bee = 100 if self.bee + value > 100 else self.bee + value
        elif meal == "grass":
            self.elephant = (
                100 if self.elephant + value > 100 else self.elephant + value
            )
            self.bee = 0 if self.bee - value < 0 else self.bee - value
        else:
            print(
                "The bee eats nectar, and the elephant eats grass. "
                "Choose one of the two"
            )


bee = BeeElephant(61, 39)

bee.eat("nectar", 50)
print(bee.bee)
print(bee.elephant)
print(bee.fly())
print(bee.trumpet())
