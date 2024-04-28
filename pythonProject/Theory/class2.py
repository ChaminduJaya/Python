class MyClass:
    y = 10  # Class variable

    @classmethod
    def update_y(cls, value):
        cls.y += value

MyClass.update_y(30)
MyClass.update_y(30)
print(MyClass.y)  # Output: 70


class MyClass:
    y = 10  # Class variable

    def __init__(self):
        MyClass.y = 30  # Update class variable

obj1 = MyClass()
obj2 = MyClass()

print(MyClass.y)  # Output: 30 (changes made by instances affect all instances but not the class)


class MyClass:
    def __init__(self, x):
        self.x = x  # Instance variable

    @classmethod
    def print_x(cls, obj):
        print(obj.x)  # Accessing instance variable x from obj

# Creating instances of MyClass
obj1 = MyClass(10)
obj2 = MyClass(20)

# Calling the class method to print the value of x for each instance
MyClass.print_x(obj1)  # Output: 10
MyClass.print_x(obj2)  # Output: 20
