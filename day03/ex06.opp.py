# 객체지향 클래스

class Dog : 
    # 생성자
    def __init__(self,name):
        self.name = name
    
    def bark(self): # 첫 번째 파라미터 self
        print(f"{self.name}가 짖습니다 멍멍")

poppy = Dog("뽀삐")
poppy.bark()

choco = Dog("초코")
choco.bark()