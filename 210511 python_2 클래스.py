class Man(object):
    cnt = 0

    @staticmethod  ##@가 붙은 것을 '장식자'라고 한다
    def get_cnt1():
        return Man.cnt

    @classmethod 
    def get_cnt2(cls):
        return Man.cnt

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Man.cnt += 1
        print( 'Man __init__ ')

    def __del__(self):
        Man.cnt -= 1
        print( 'Man __del__ ')

    def __str__(self):
        return '{}님은 {}살'.format(self.name, self.age)

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False

    def __add__(self, num):
        self.age = self.age + num

    def __sub__(self, num):
        self.age -= num

    def disp_Man(self):
        print( '{}님은 {}살'.format(self.name, self.age))

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def sset_age(self, age):
        self.age = age



print('현재 객체 생성 수는 : {}'.format(Man.cnt))
print('현재 객체 생성 수는 : {}'.format(Man.get_cnt1()))


m1 = Man('손흥민', 30)
m2 = Man('이강인', 21)
m3 = Man('손흥민', 30)

print('현재 객체 생성 수는 : {}'.format(Man.cnt))
print('현재 객체 생성 수는 : {}'.format(Man.get_cnt2()))
print('현재 객체 생성 수는 : {}'.format(m1.get_cnt2()))jj


# print(m1) ##st함수 자동 호출
# print(m2)
# print(m1.__str__()) ##2줄 위의 내용과 같다.
# print(m2.__str__())
print(m1 == m3)
print(id(m1) == id(m3))
m1 + 2
m2 - 3
m1.disp_Man()
m2.disp_Man()