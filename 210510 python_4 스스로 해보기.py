class It(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return('{}는 {}살 입니다.'.format(self.name, self.age))

    def __add__(self, num):
        self.age = self.age + num

    def __sub__(self, num):
        self.age = self.age - num

    def __eq__(self, other):
        if self.name == self.other and self.age == self.other:
            print(True)

        else:
            print(False)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self):
        return self.name

    def set_age(self):
        return self.age

it1 = It('호호', 20)
it2 = It('히히', 10)

print(it1)
print(it2)
    