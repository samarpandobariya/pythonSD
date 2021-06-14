class Demo:
    def myfunction(self):
        print("This is my fucation of class...")


    def show(self,name):
        print("value is : ",name)

    def __init__(self ,nm):
        print("This is demo class... ")
        print("Name is :",nm)

d1=Demo("abc")
d1.myfunction()
d1.show("Jay")