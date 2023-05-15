from Principles.Abstraction_and_Polymorfism.shape import Shape
import math  

class Triangle(Shape):

    def __init__(self, xy, yz, xz, height = None):
        # base = xy
        self.xy = xy
        self.yz = yz
        self.xz = xz
        self.height = height
    
     def area(self):
        if self.height is None:
            area = 0.25 * math.sqrt(self.xy + self.yz + self.xz) * \
                                 math.sqrt(-self.xy + self.yz + self.xz) * \
                                 math.sqrt(self.xy - self.yz + self.xz) * \
                                 math.sqrt(self.xy + self.yz - self.xz) * \
            return area
        else:
            return self.xy * self.height/2

    def perimeter(self):
        return self.xy + self.yz + self.xz