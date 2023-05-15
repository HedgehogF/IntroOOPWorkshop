from Principles.Inheritance.animales.animal import Animal
from Principles.Inheritance.animales.dog import Dog

animal = Animal("Generic animal")
animal.speak()

# Create an instance of the subclass
dog = Dog("Fido", "Golden Retriever")
dog.speak()
print(dog.breed)