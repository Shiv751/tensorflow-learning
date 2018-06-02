class MyDemo:
    def add(self, x, y):
        print("Addition of ", x," and ",y," is ", x+y)
        return x + y
    def minus(self, x, y):
        print("X is = ", x)
        print("Y is = ", y)
        return x-y

    def multiply(self, x, y):
        print("X is = ", x)
        print("Y is = ", y)
        return x*y

    def divide(self, x, y):
        print("X is = ", x)
        print("Y is = ", y)
        return x/y

    def square(self, x, y):
        print("X is = ", x)
        print("Y is = ", y)
        return x**y


obj = MyDemo()
print(obj.add(9, 8))
print(obj.minus(9, 8))
