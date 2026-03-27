# ex01.variable.py

# 여러줄 주석은 여러줄 문자열로 대체 사용
'''
여러줄 문자열을 
주석처럼 사용

**자료형**
정수 int 
실수 float
문자열 str 
불린 bool
None(NoneType)
그 외 클래스 타입
'''
# val = "'hello'"  # 특수문자 \n.\t,\',\" 지원
val = False
print(val)
print(type(val))

age = 28
print("나이는 "+str(age))
print("나이는 "*age)
print("나이는 ",age,"입니다")

이름 = input("이름 > ")
나이 = int(input("나이 > "))
키 = float(input("키 > "))

print("이름 : ",이름,"나이 : ",나이,"키 : ",키)
