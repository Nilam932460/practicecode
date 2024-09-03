class institute:
    def display(self):
        print('main Branch')
        
class Branch1(institute):
    def print(self):
        print('kalyan Branch')

class Branch2(institute):
     def show(self):
         print('Dombivali Branch')

b1=Branch1()
b1.print()
b1.display()

b2=Branch2()
b2.show()
b2.display()

