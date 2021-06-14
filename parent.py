class Parent:

    def fun1(self):
        print("This method is parent.......")

class Child(Parent):

        def fun2(self):
            print("This method is child.......")

c1 = Child()
c1.fun1()
c1.fun2()