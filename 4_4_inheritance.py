class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is making a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog = Dog("Buddy", "Labrador")

dog.speak()
