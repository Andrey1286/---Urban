class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')  # Открываем для чтения
        products_str = file.read()  # Читаем содержимое файла
        file.close()  # Закрываем файл
        return products_str

    def add(self, *products):
        file_1 = open(self.__file_name, 'r')
        file_text = file_1.read()
        file_1.close()
        for product in products:
            if str(product) in file_text:
                print(f'Продукт {str(product)} уже есть в магазине')
            else:
                file_1 = open(self.__file_name, 'a')
                file_1.write(f"{str(product)}\n")
                file_1.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

