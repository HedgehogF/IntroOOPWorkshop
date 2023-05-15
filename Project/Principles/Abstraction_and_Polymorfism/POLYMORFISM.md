# POLYMORFISM

Polymorphism is the ability of objects to take on different forms depending on the context in which they are used. In Python, polymorphism is achieved through the use of method overloading, method overriding, and duck typing.

Method overloading allows a class to have multiple methods with the same name but different signatures (i.e., different numbers or types of arguments). Python does not support method overloading in the traditional sense, but you can achieve similar behavior by using default arguments or variable-length argument lists.

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

shapes = [Circle(5), Rectangle(3, 4)]

for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
```

In this example, we define two concrete classes Circle and Rectangle that inherit from the abstract class Shape. Each class provides its own implementation of the area and perimeter methods based on its specific shape.

We then create a list of shapes that contains an instance of Circle and an instance of Rectangle. We can then iterate over the list and call the area and perimeter methods on each shape, without needing to know the specific class of each shape. This demonstrates the idea of duck typing and dynamic polymorphism, where objects that have the same interface can be used interchangeably, regardless of their actual class or type.

BACK TO [README](/README.md)