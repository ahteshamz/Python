#Add a static method in problem 2, to greet the user with Hello!

#Write a class "Calculator" capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square is: {self.num * self.num}")
    def cube(self):
        print(f"The cube is: {self.num * self.num * self.num}")
    def squareroot(self):
        print(f"The squareroot is: {self.num ** 0.5}")

    @staticmethod
    def  hello():
        print("Hello there!")
a = Calculator(25)
a.hello()
a.square()
a.cube()
a.squareroot()