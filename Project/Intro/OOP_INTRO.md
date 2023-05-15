
# OOP INTRO

## CLASS

### What is a class?

A class is a blueprint for creating **objects**, providing **initial values** for state and implementations of **behaviour**.

Objects -> An instance of a class

Initial Values -> variables or attributes

Behaviour -> functions or methods

Class in Python:
```python
class Human:
    pass
```

![class image](/Project/class_object.svg)

## Variables

1. **Instance Variables** that are defined inside `__init__` are called instance variables.
2. **Class/Static Variables** that are defined outside the `__init__`.
3. **Local Variables** that are confined to a method.
```python
class Human:
    
    tribe = "Hominina"

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
     
    def describe(self):
        description = f"My name is {self.first_name} {self.last_name}  and I am {self.age} years old."
        print(description)
```
> **tribe** variable is a class variable

> **first_name**, **last_name** and **age** (which start with self.) variables are **Instance Variables**
 
> **description** variable is local variable
> 
## Functions vs Methods

**A function** is a set of instructions or procedures to perform a specific task.

**A Method** is **a function** that is associated with an object.
1. A method is implicitly passed the object on which it was called.
2. A method is able to operate on data that is contained within the class

## Methods

### Instance methods

These methods are only accessible through class objects.

```python
class Human:

    tribe = "Hominina"

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe(self):
        description = f"My name is {self.first_name} {self.last_name}  and I am {self.age} years old."
        print(description)


john = Human("John","Doe",30)
john.describe()
```
In the above example `describe` method is an instance method. This method is only accessible through class object `jhon`. 

### Class methods

These methods can be called directly using the class name instead of creating an object of that class.

To declare a class methods in Python, we need to use the `@classmethod` decorator.
```python

class Human:

    tribe = "Hominina"

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe(self):
        description = f"My name is {self.first_name} {self.last_name}  and I am {self.age} years old."
        print(description)

    @classmethod
    def getTribe(cls):
        return cls.tribe

print(Human.getTribe())
```
In the above example `getTribe` is a class method. We call it by using the class name instead of creating an object of the class.

### Static methods

These methods are usually used as a utility function. These methods do not have any relation to the class variables and instance variables. (Are **NOT** allowed to modify the class attributes inside a static method)
```python

class Human:

    tribe = "Hominina"

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe(self):
        description = f"My name is {self.first_name} {self.last_name}  and I am {self.age} years old."
        print(description)

    @classmethod
    def getTribe(cls):
        return cls.tribe

    @staticmethod
    def human_wikipedia_definition():
        print("Humans (Homo sapiens) are the most common and widespread species of primate in the great ape family Hominidae.")


john = Human("John","Doe",30)
john.human_wikipedia_definition()

Human.human_wikipedia_definition()
```

## Constructor
**Constructor** are generally used for instantiating/creating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created.

Constructors in Python

```python
class Human:

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
john = Human("John","Doe",30)
```