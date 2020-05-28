class Product:
    my_type = ""
    name = ""
    price = 0

    def __init__(self, my_type, name, price):
        if type(my_type) != str:
            raise ValueError("Type should be a string")
        if type(name) != str:
            raise ValueError("Type should be a string")
        if type(price) != int and type(price) != float:
            raise ValueError("Price should be a number")

        self.my_type = my_type
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} = {self.price}'

    def __repr__(self):
        return f'{self.name} = {self.price}'


class ProductStore:
    amount = 0
    profit = 0
    storage = []
    store_type = ""
    store_name = ""
    store_price = 0

    def __init__(self, *args):
        if len(args) != 0:
            for item in args:
                for key in item:
                    if key == "type":
                        self.store_type = item[key]
                    elif key == "name":
                        self.store_name = item[key]
                    elif key == "price":
                        self.store_price = item[key]
                    elif key == "amount":
                        self.amount = item[key]
                self.temporary_object = Product(self.store_type, self.store_name, self.store_price)
                self.add(self.temporary_object, self.amount)

    def add(self, product, amount):
        x = {}
        x["product"] = product
        x["amount"] = amount
        product.price *= 1.3
        self.storage.append(x)

    def set_discount(self, identifier, percent, identifier_name):
        if type(percent) != int and type(percent) != float:
            raise ValueError("Percent should be a number")
        identifier_name = identifier_name.lower()
        if identifier_name == "type":
            for i in self.storage:
                my_product = i["product"]
                if my_product.my_type == identifier:
                    my_product.price = my_product.price * (1 - (percent / 100))
        elif identifier_name == "name":
            for i in self.storage:
                my_product = i["product"]
                if my_product.name == identifier:
                    my_product.price = my_product.price * (1 - (percent / 100))
        else:
            raise ValueError("Identifier_name should be a 'type' or 'name' ")

    def sell_product(self, product_name, amount):
        for i in self.storage:
            my_product = i["product"]
            if my_product.name == product_name:
                if amount > i["amount"]:
                    raise CustomException("We don't have such amount of product")
                else:
                    i["amount"] -= amount
                    self.profit += (amount * my_product.price)

    def get_income(self):
        return f"{self.profit} $"

    def get_all_product(self):
        return self.storage

    def product_info(self, product):
        for i in self.storage:
            my_product = i["product"]
            if my_product.name == product.name:
                my_tuple = product.name, i["amount"]
                return my_tuple


class CustomException(Exception):
    message = ""

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return f'{self.message}'

    def __repr__(self):
        return f'{self.message}'


try:
    first_product = Product("fruit", "apple", 10)
    second_product = Product("fruit", "watermelone", 45)

    test_product = {"type": "fruit", "name": "pear", "price": 10, "amount": 200}
    test_product2 = {"type": "vegetable", "name": "onion", "price": 5, "amount": 135}
    store = ProductStore(test_product, test_product2)
    print(store.get_all_product())

    store.add(first_product, 200)
    store.add(second_product, 50)
    print(store.get_all_product())
    store.sell_product("apple", 12)
    store.sell_product("watermelone", 30)
    print(store.get_all_product())
    print(store.get_income())
    store.set_discount("fruit", 50, "type")
    print(store.get_all_product())
    print(store.product_info(first_product))
except ValueError as e:
    print(e)
except CustomException as e:
    print(e)
