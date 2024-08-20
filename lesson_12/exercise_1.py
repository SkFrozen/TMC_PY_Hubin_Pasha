class Product:

    def __init__(self, name: str, shop_name: str, cost: float):
        self.__name = name
        self.__shop_name = shop_name
        self.__cost = cost

    def __add__(self, other):
        return self.__cost + other.get_props["cost"]

    def __str__(self):
        return f"{self.get_props}"

    @property
    def get_props(self) -> dict:
        product = {
            "name": self.__name,
            "shop": self.__shop_name,
            "cost": self.__cost,
        }
        return product


class StoreHouse:

    def __init__(self, products):
        self.__products = products

    def __getitem__(self, index: int) -> dict:
        if index >= len(self.__products):
            return f"The product doesn't exist. You only have {len(self.__products)} products"
        return self.__products[index]

    def __str__(self) -> str:
        return f"{[product.get_props for product in self.__products]}"

    def get_product_by_name(self, name: str) -> dict:
        for product in self.__products:
            if product.get_props.get("name").lower() == name.lower():
                return product
        return "The product wasn't found"

    def sort_products_by_value(self, value, decrease=False):
        if value in ("name", "shop", "cost"):
            self.__products = sorted(
                self.__products,
                key=lambda product: product.get_props.get(value),
                reverse=decrease,
            )
        else:
            print("Enter correct value: name, shop or cost")

    def total_amount_products(self):
        return sum([product.get_props.get("cost") for product in self.__products])


axe = Product("Axe", "Mega-Mall", 15.25)
t_short = Product("T-short", "Milavitsa", 230.99)
shoes = Product("Shoes", "Mega-top", 199.99)

store_house = StoreHouse([axe, t_short, shoes])
print(store_house[1])
store_house.sort_products_by_value("cost")
print(store_house)
print(store_house.get_product_by_name("aXe"))
print(store_house.total_amount_products())
