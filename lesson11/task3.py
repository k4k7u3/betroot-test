class Product:
    type_product = ''
    name_product = ''
    price = 0
    amount = 0
    all_type_products = []
    categories_of_product = []
    product_and_amount = {}
    product_and_price = {}
    profit = 0

    def __init__(self, type_product, name_product, price, amount):
        self.type_product = type_product
        self.name_product = name_product
        self.price = price
        self.amount = amount
        Product.all_type_products.append(self.type_product)
        Product.product_and_amount[self.name_product] = self.amount
        Product.product_and_price[self.name_product] = self.price * 1.3


class ProductStore(Product):
    def __init__(self):
        pass

    def add(self, name_product, price, amount):
        self.product_and_amount[name_product] = amount
        self.product_and_price[name_product] = (price * 1.3)

    def set_discount(self, name_product, discount):
        self.discount = 1 - (discount / 100)
        if name_product in self.product_and_price:
            self.old_price =  self.product_and_price[name_product]
            self.product_and_price[name_product] = self.old_price * self.discount
        else:
            print("We don't have this product")

    def sell_product(self, name_product, amount):
        try:
            if amount > self.product_and_amount[name_product]:
                raise ValueError("We don't have a such an amount of products!")
            else:
                if name_product in self.product_and_amount:
                    self.temporary_amount = self.product_and_amount[name_product]
                    self.product_and_amount[name_product] = self.temporary_amount - amount
                    self.profit = amount * self.product_and_price[name_product]
                else:
                    print("We don't have this product")
        except ValueError as e:
            print(e)

    def get_income(self):
        return self.profit

    def get_all_products(self):
        return self.product_and_amount, self.product_and_price


x = Product('sport', 'ball', 30, 100)
print('Product and amount', x.product_and_amount)
print('Product and price', x.product_and_price)
y = ProductStore()
y.add('Shampoo', 30, 300)
print('Product and amount', y.product_and_amount)
print('Product and price', y.product_and_price)
y.set_discount('Shampoo', 10)
print('Product and price', y.product_and_price)
y.sell_product('Shampoo', 20)
print('Product and amount', y.product_and_amount)
print('Profit: ', y.get_income())
name_amount, name_price = y.get_all_products()
for i in name_amount and name_price:
    print(f'Product: {i} - {name_amount[i]} pieces. Price: {name_price[i]} UAH apiece')
