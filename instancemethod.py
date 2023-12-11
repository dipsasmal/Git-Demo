class Product:
    def __init__(self):
        self.name='Android'
        self.description='it is awesome'
        self.price=10000

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)

p=Product()
p.display()