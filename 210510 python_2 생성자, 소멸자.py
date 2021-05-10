class Korea(object):
    def __init__(self, city, pop): ##생성자 함수
        self.city = city
        self.pop = pop
        print('Korea__int__: 생성자')

    def __del__(self): ##소멸자 함수
        print('Korea__del__: 소멸자')

    def ___str__(self):
        return "{}인구는 ==> {}만명".format(self.city, self.pop)

    def disp_Korea(self):
        print(self.city, '인구는', self.pop, '만명')

    def get_city(self):
        return self.city

    def get_pop(self):
        return self.pop

    def set_city(self, city):
        self.city = city

    def set_pop(self, pop):
        self.pop = pop


      #위에는 class 선언  

# print('###############')
# def ff():
#     print('나는 함수다')

#ff()
# 위에는 함수 선언

k1 = Korea('서울시', 950)  ##k1의 id값이 self로 넘어가는데 이때 id값은 보이지 않는다.
k2 = Korea('부산시', 700)  ## 객체가 함수를 불러올 때는 id값을 보이지 않게 넘어가는데 이때 id값을 저장하는 것이 self
k2.pop = 360

k1.disp_Korea()
k2.disp_Korea()

k1.city = '수원시'
k1.pop = 110

print(k1.get_city(), k1.get_pop())
print(k2.get_city(), k2.get_pop())

print(k1.__str__())
print(k1)
print(k2.__str__())
print(k2)


