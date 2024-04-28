class python:
    pass  # can't keep class empty


class Java:  # different class can be created

    count = 0  # class level attribute

    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age
        self.instance = 89
        Java.count += 1
        print(name)

    def update(self, name, age):  # instance method. called only by object
        self.name = name  # instance attribute
        self.age = age
        print(name, age)

    @classmethod #this must be here. because though there is clsss or anything instead of cls.. no error. we can include self also..so how
                # we identify whether class level or instance...from @classmethod
    def counter(cls):  # class level method
        cls.count += 1
        Java.count += 1
        print('count',cls.count)

    def manyArgs(selfff, *arg):
        print('arg[0]', arg[0])
        print(len(arg))
        print(arg)
        return arg[1] + arg[2]
    # def hello(value): hello called by obj. so there must be self. Because obj also coming as argument.
    #   print('hello')


obj = Java('cham', 17)
obj2 = Java('chamiiii', 17)
obj.update('ddffdss', 6778)
obj2.update('ddffdss', 6778)
asr = obj.manyArgs(1, 2, 3)
# obj.hello(34)# from this, two arguments were given. one is obj and other one is 34
Java.counter()
