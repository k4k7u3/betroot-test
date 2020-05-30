import json

json_info = None


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
    storage_json = []
    store_type = ""
    store_name = ""
    store_price = 0

    def __init__(self, *args):
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
        product.price = round(product.price, 2)
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
                    if i["amount"] == 0:
                        self.storage.remove(i)

    def get_json(self):
        for item in self.storage:
            temporary_dict = {}
            my_product = item["product"]
            temporary_dict["type"] = my_product.my_type
            temporary_dict["name"] = my_product.name
            temporary_dict["price"] = my_product.price
            temporary_dict["amount"] = item["amount"]
            self.storage_json.append(temporary_dict)
        return self.storage_json

    def set_profit(self, input_profit):
        self.profit = input_profit

    def get_profit(self):
        return self.profit

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


def unpack_json(json_info):
    for item in json_info:
        for key in item:
            if key == "type":
                json_type = item[key]
            if key == "name":
                json_name = item[key]
            if key == "price":
                json_price = item[key]
            if key == "amount":
                json_amount = item[key]
        temporary_product = Product(json_type, json_name, json_price)
        my_product_store.add(temporary_product, json_amount)


def unpack_json_profit(json_info):
    json_profit = json_info
    my_product_store.set_profit(json_profit)


def input_check(input_str):
    my_str = input_str.replace(".", "")
    if my_str.isdigit():
        if input_str.count(".") == 0:
            return int(input_str)
        elif input_str.count(".") == 1:
            return float(input_str)
        else:
            return "error"


try:
    try:
        json_file = open("mystore.json", "r")
        json_info = json.load(json_file)
    except json.decoder.JSONDecodeError:
        json_info = []
    json_file.close()

    my_product_store = ProductStore()
    unpack_json(json_info)

    try:
        json_file = open("myprofit.json", "r")
        json_info = json.load(json_file)
    except json.decoder.JSONDecodeError:
        json_info = []
    json_file.close()

    unpack_json_profit(json_info)

    while True:
        try:
            input_choise = input("Choose, what do you want to do? (1 - add new product; 2 - sell product; 3 - add discount; 4 - show your store; 9 - close store) ")
            input_choise = input_choise.strip().lower()
            if input_choise == '1':
                input_type = input("Please, input type of product: ")
                input_name = input("Please, input name of product: ")
                while True:
                    input_price = input("Please, input price per unit of product: ")
                    if input_price.isdigit():
                        input_price = int(input_price)
                        break
                    else:
                        print("Price should be a number")
                        continue
                while True:
                    input_amount = input("Please, input amount of product: ")
                    input_amount = input_check(input_amount)
                    if input_amount == "error":
                        print("Percent should be a number")
                        continue
                    else:
                        break
                input_product = Product(input_type, input_name, input_price)
                my_product_store.add(input_product, input_amount)
                continue
            elif input_choise == '2':
                input_name = input("Input name of product you want to sell: ")
                while True:
                    input_amount = input("Input amount: ")
                    if input_amount.isdigit():
                        input_amount = int(input_amount)
                        break
                    else:
                        print("Amount should be a number")
                        continue
                my_product_store.sell_product(input_name, input_amount)
                continue
            elif input_choise == '3':
                while True:
                    input_identifier_name = input("Input identifier name (type, or name): ")
                    input_identifier_name = input_identifier_name.strip().lower()
                    if input_identifier_name != "type" and input_identifier_name != "name":
                        print("Identifier name should be a 'type' or 'name' ")
                        continue
                    else:
                        break
                if input_identifier_name == "type":
                    input_name = input("Input type of product you want to sell: ")
                elif input_identifier_name == "name":
                    input_name = input("Input name of product you want to sell: ")
                while True:
                    input_percent = input("Input percent of discount: ")
                    input_percent = input_check(input_percent)
                    if input_percent == "error":
                        print("Percent should be a number")
                        continue
                    else:
                        break
                my_product_store.set_discount(input_name, input_percent, input_identifier_name)
                continue
            elif input_choise == '4':
                print("This is your store: ")
                print(f"{my_product_store.get_all_product()}")
                print(f"Income: {my_product_store.get_income()}")
                continue
            elif input_choise == '9':
                json_info = my_product_store.get_json()
                print("Our store is closing. See you tomorrow.")
                break
        except ValueError as e:
            print(e)
            continue
        except CustomException as e:
            print(e)
            continue
except Exception as e:
    print(e)
finally:
    with open('mystore.json', 'w+') as json_file:
         json.dump(json_info, json_file, indent=4)
    json_info = my_product_store.get_profit()
    with open('myprofit.json', 'w+') as json_file:
         json.dump(json_info, json_file, indent=4)
print("Good Bye")

