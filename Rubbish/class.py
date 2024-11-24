class Person:

    def __init__(self, name, age):
        self.name = name  # имя человека
        self.age = age  # возраст человека

    def PrintAll(self):
        print(self.age)


tom = Person("Tom", 22)

tom.PrintAll()