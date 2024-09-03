class Animal:
    def walk(self):
        print('hello,i am from parent')

class dog(Animal):
    def walk(self):
        print('hello, i am from child')

x=Animal()
x.walk()
y=dog()
y.walk()
