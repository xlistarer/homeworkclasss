# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
Task 1

School

Make a class structure in python representing people at school. Make a base class called Person, a class called Student, and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not. For example, the name should be a Person attribute, while salary should only be available to the teacher.

'''
class Person():
    pass





'''
Task 2

Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
```

class Mathematician:

    pass

 

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
'''
class Mathematician:
    def square_nums (self,args):
         try:
            return [i*i for i in args]
         except:
            print('mathemetican work only with numbers')

    def remove_positives(self,args):
        try:
            return [i for i in args if i<=0]
        except:
            print('mathemetican work only with numbers')

    def filter_leaps(self,args):
        try:
            return [i for i in args if i%4==0 and i%100!=0]
        except:
            print('mathemetican work only with numbers')


m=Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

'''
Task 3

Product Store

Write a class Product that has three attributes:

type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store. All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

class Product:

    pass

class ProductStore:

pass

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product(Food, 'Ramen, 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell(‘Ramen’, 10)

assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)



'''
class Product:

    def __init__(self, type,name,price):
        self.type=type
        self.name=name
        while True:
            try:
                float(price)
                if price<0:
                    raise Exception
                self.price=float(price)
            except:
                price=input('only numbers more than nul')

class Store:
    def __init__(self, type):
        self.type=type
        self.products={}
    def add(self,product, count):
        if product.name in self.products:
            self.products[product.name]+=count
        else:
            self.products.update({product.name:count})

    def sell(self,product, count):
        if product.name in self.products:
            if self.products[product.name]>=count:
                self.products[product.name] -= count
            else:
                print('there is not enough')
        else:
            print('we havent this product')
    def set_discount(self,identifier, percent, identifier_type='name'):
        if identifier_type=='name':
            pass

    def get_income()
    def  get_all_products()
    def get_product_info(product_name)

