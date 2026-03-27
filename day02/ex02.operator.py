# ex05_operator.py 연산자 학습

a = 15
b = 14

print("덧셈 = ", a+b)
print("뺄셈 = ", a-b)
print("곱셈 = ", a*b)
print("나눗셈 = ", a/b) # 결과 항상 float
print("몫 = ", a//b)    # 정수
print("나머지 = ", a%b) # 정수
print("거듭제곱 = ", a**b)

x = 10
print(x)

x += 5
print(x)

print("a==b : ",a==b)
print("a>b : ",a>b)
print("a<b : ",a<b)

# 논리연산
age = 19
is_license =  True 
print("나이는 20세 이상이고 면허증 소지 ? ",age >=20 and is_license == True)
print("나이는 20세 이상이고 면허증 소지 ? ",age >=20 and is_license)

print("나이는 20세 이상이거나,면허증 소지 ? ",age >=20 or is_license==True)

# 멤버 연산
fruits =['사과','바나나','망고','포도']
sentence = "파이썬은 쉬워요"

print("과일 중 바나나 존재 여부 : ","바나나" in fruits) 
print("과일 중 수박 존재 여부 : ","수박" in fruits) 
print("문장 내 '파이썬'단어 여부 : ","파이썬" in sentence) 