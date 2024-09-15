from fileinput import close
from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

        print(str(self))
    def __str__(self):
        return f"{self.name} , {self.weight} , { self.category}"

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file1 = open(self.__file_name, "r")
        o = ""
        for h in file1.read():
           o = o + h
        file1.close()
        return o
    def add(self, *args):
        file = open(self.__file_name, "a")
        file2 = open(self.__file_name, "r")
        for i in range(len(args)):
            if f'{(args[i])}\n' in file2:
                print(f'Продукт {(args[i])} уже есть в магазине')
            else:
                file.write(f'{(args[i])}\n')
        file.close()
        file2.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())