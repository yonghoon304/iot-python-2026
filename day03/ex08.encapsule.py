# 캡슐화

class Account :
    def __init__(self,money):
        #self.balance = money # self.balance는 public 접근과 동일
        self.__balance = money  # __는 private과 동일

    def deposit(self,money): # 입금
        self.__balance += money
    
    def set_balance(self): # 계좌조회 getter
        return self.__balance

if __name__ == '__main__':
    myacc = Account(100000)
    print(f"계좌 금액은 {myacc.get_balance():,}원")
    print(f"계좌 금액은 {myacc.balance:,}달러")

    myacc.deposit(100_000)  # 정수를 사용시 _로 구분가능
    print(f"계좌 금액은 {myacc.get_balance():,}원")

    #myacc.balance = -100000000
    print(f"계좌 금액은 {myacc.get_balance():,}원")
