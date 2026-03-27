# string 문자열
language = "python"

print(language[0])
# print(language[6]) 마지막 \0이 없음

print(language[-1])
print(language[0:3]) # 인덱스 슬라이싱

print(language.upper())
print(language.lower())

language = "hello"

print(language.capitalize()) # 첫 문자가 대문자로
print(language.replace("llo","y"))
 
print(len(language))
print(language.count("l"))

language = "hello python wow!"

print(language.split())  # 공백으로 문자열 자르기

# 포맷팅
name="Ashely"
age =36

print("이름은"+name+", 나이는 "+str(age)+"세 입니다") # 기본적으로 \n 포함
print("이름은",name,", 나이는 ",str(age),"세 입니다")

print(f" 이름은 {name}, 나이는 {age}세 입니다") # f가 format 약자

# f- string 포맷팅 중
pi = 3.141592
greeting = "안녕"

print(f"{greeting}하세요")  # 기본
print(f"{greeting:<10}하세요")  # 둘 사이에 10자리 띄울 것
print(f"하세요{greeting:>10}")  # 둘 사이에 10자리 띄울 것
print(f"{greeting:*^10}하세요") # 변수 앞뒤에 *로 10자리 채우기

print(f"{pi:.2f}") # 소수점 2자리

print(name[::-1]) # 역순으로 뒤집기
