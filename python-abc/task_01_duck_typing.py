#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return 3.14 * self.rad ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.rad

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
def shape_info(obj):
    print(obj.area())
    print(obj.perimeter())
