from abc import abstractmethod, ABC

class Shape(ABC):
    def accept(self):
        self.x=int(input('enter x value'))
        self.y=int(input('enter y value'))

    @abstractmethod
    def area(self):
      pass

class Rectangle(shape):
     def area(self):
         print('Area of rectangle',self.x*self.y)


class Tringle(shape):
     def area(self):
         print('Area of tringle',0.5*self.x*self.y)



r1=rectangle()
t1=traingle()
r1.accept()
t1.accept()
r1.area()
t1.area()
               
