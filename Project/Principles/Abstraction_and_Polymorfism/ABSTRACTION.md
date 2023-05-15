# ABSTRACTION

Abstraction is a fundamental concept in object-oriented programming that **involves hiding the implementation details of a class from the outside world** and only exposing a simplified interface to the users of the class.

In Python, abstraction can be achieved through the use of abstract classes and interfaces. Abstract classes are classes that **cannot be instantiated** but can be **subclassed**. They are used to define a common interface that all subclasses must implement, but the implementation details are left to the subclasses themselves. Abstract classes are defined using the `abc` module in Python.

Here's an example of an abstract class:

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
```

In this example, the `Shape` class is an abstract class that defines two **abstract methods** `area()` and `perimeter()`. These methods **must** be implemented by any subclass of `Shape`, but the implementation details are left to the subclasses themselves. This allows us to define a common interface for all shapes, but the details of how each shape calculates its area and perimeter are left to the specific shape classes.

Interfaces, on the other hand, are similar to abstract classes but contain only abstract methods. They are used to define a common interface that all classes implementing the interface must adhere to. In Python, there is no separate keyword for interfaces, but you can achieve the same effect by defining an abstract base class that contains only abstract methods.

Abstraction allows you to design more flexible and extensible code by separating the interface from the implementation details. This makes it easier to change the implementation details without affecting the code that uses the interface, and it also makes it easier to extend the code with new functionality by creating new subclasses or implementing new interfaces.