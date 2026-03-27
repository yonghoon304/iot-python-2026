# 함수
# 더하기 함수
def add(a,b):
    return a+b

# 파라미터 없는 함수
def test():
    x =10
    return x

# 리턴없는 함수
def sayHello(name):
    print(f"안녕하세요 {name}")


print(add(10,9))
print(add(10,9.59))
print(add("문자열도"," 되나요"))

print("안녕하세요",end="") # end의 기본값은 \n
print("안녕히가세요")

result = add(10,4)
print(f"결과는 {result}")

sayHello("최용훈")
