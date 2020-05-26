class Product:
    my_type = ""
    name = ""
    price = 0

    def __init__(self, my_type, name, price):
        if type(my_type) != str:
            raise ValueError("Type should be a string")
        else:
            self.my_type = my_type
        if type(name) != str:
            raise ValueError("Type should be a string")
        else:
            self.name = name
        if type(price) != int and type(price) != float:
            raise ValueError("Price should be a number")
        else:
            self.price = price

    def __str__(self):
        return f'{self.name} = {self.price}'

    def __repr__(self):
        return f'{self.name} = {self.price}'


class ProductStore:
    amount = 0
    profit = 0
    storage = []

    def add(self, product, amount):
        x = {}
        x["product"] = product
        x["amount"] = amount
        product.price *= 1.3
        self.storage.append(x)

    def set_discount(self, product_identifier, percent):
        if type(percent) != int and type(percent) != float:
            raise ValueError("Percent should be a number")
        for i in self.storage:
            my_product = i["product"]
            if my_product.my_type == product_identifier or my_product.name == product_identifier:
                my_product.price = my_product.price * (1 - (percent / 100))

    def sell_product(self, product, amount):
        for i in self.storage:
            my_product = i["product"]
            if my_product.name == product.name:
                try:
                    if amount >= i["amount"]:
                        raise Exception("We don't have such amount of product")
                    else:
                        i["amount"] -= amount
                        self.profit = amount * my_product.price
                except Exception as e:
                    print(e)

    def get_income(self):
        return print(f"{self.profit} $")

    def get_all_product(self):
        return print(self.storage)

    def product_info(self, product):
        for i in self.storage:
            my_product = i["product"]
            if my_product.name == product.name:
                my_tuple = product.name, i["amount"]
                return print(my_tuple)

try:
    first_product = Product("fruit", "apple", 10)
    second_product = Product("fruit", "watermelone", 45)
    store = ProductStore()
    store.add(first_product, 200)
    store.add(second_product, 50)
    store.get_all_product()
    store.sell_product(first_product, 10)
    store.get_all_product()
    store.get_income()
    store.set_discount("apple", 20)
    store.get_all_product()
    store.product_info(first_product)
except ValueError as e:
    print(e)
