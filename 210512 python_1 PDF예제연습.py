'''
class Smart(object):
    cnt = 0
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        print(" Smart __int__")

    def __del__(self):
        print(" Smart __del__ ")

    def Disp(self):
        print(" 모델: ", self.model, "색상 : ", self.color, "가격 : ", self.price, "원")


s1 = Smart("갤럭시8", "골드", 900000)
s2 = Smart("아이폰8", "블랙", 950000)
'''

class Smart(object):
    cnt = 0
    def __init__(self, model, color, price):
        
