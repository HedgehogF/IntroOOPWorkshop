# INHERITANCE

**Inheritance** is a fundamental feature of object-oriented programming that allows a new class to be based on an existing class. The new class **inherits the properties and methods of existing class**, and can also **add new properties and methods of its own**.

The existing class is called the **superclass** or **parent class**, and the new class is called the **subclass** or **child class**.
[Animal](animales/animal.py)
```python
# Define a superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says hi!")


# Define a subclass that inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks!")


# Create an instance of the superclass
animal = Animal("Generic animal")
animal.speak()

# Create an instance of the subclass
dog = Dog("Fido", "Golden Retriever")
dog.speak()
print(dog.breed)
```
![Image](\assets\Inheritance.png)

In this example, we define a superclass `Animal` with a constructor and a `speak` method.
We then define a subclass `Dog` that inherits form `Animal` and adds a new `breed` attribute and overrides the `speak` method. We create an instance of the superclass and call its `speak` method, and then create an instance of the subclass and call its `speak` method and print its `breed` attribute.

Output:
```commandline
Generic animal says hi!
Fido barks!
Golden Retriever
```

As you cand see, the `Dog` subclass inherits the `__init__` and `speak` methods from the `Animal` superclass, and we can also add new attributes and override the existing ones in the subclass.


Another Example:
![Image2](/person/uml_diagram.png)