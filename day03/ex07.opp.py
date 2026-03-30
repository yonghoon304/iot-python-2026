# 객체 상속

class Animal:   # 동물 클래스
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("소리를 낸다")

class dog(Animal):  # 동물 클래스 상속한 개 클래스
    def speak(self):    # 오버라이딩
        print(f"{self.name},멍멍")

class Cat(Animal):
    def speak(self):    # 오버라이딩
        print(f'{self.name},야옹')

poppy = dog("뽀삐")
poppy.speak()

nabi = Cat("나비")
nabi.speak()