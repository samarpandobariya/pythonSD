class Parent:

    def fun1(self):
        print("This method is parent.......")

class Child(Parent):

        def __init__(self) :
            print("This is child class value ")

        def fun2(self):
            print("This method is child.......")


class Child1 (Child):

        def fun3(self):
            print("This is child method to call....")

c1 = Child1()
c1.fun1()
c1.fun2()
c1.fun3()