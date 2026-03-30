# 예외처리

num = int(input("나눌 분모 입력 > "))

# 예외가 발생할 것으로 추축되면 위치를 try로 감싼다
try:
    res = 100/num
    print(f"100/{num}= {res}")
except ZeroDivisionError as e :
    print("0은 쓰지 마세요")
except ValueError as e :
    print("숫자만 넣으세요")  #숫자대신 문자를 입력할 때 예외를 나눠서 처리
except Exception as e: #예외클래스 인스턴스 e 생성
    print(e.args)
else : # 예외가 발생 안했을때만 처리
    print("프로그램 정상 종료")
finally : # 옵션
    print("예외 유무관계없이 실행")

print("끝") # 정상적으로 종료되면 출력