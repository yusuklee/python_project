def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print('0으로 나눌수 없습니다.')
    else:
        return a/b
    
def cal_bmi(weight,height):
    if(height==0):
        return "키에 0을 넣지 마시오."
    bmi=weight/(height**2)
    return round(bmi,2)

def show_menu(): 
    print('\n===계산기 메뉴===')
    print('1.덧셈')
    print('2.뺄셈')
    print('3.곱셈')
    print('4.나눗셈')
    print('5.bmi 계산')
    print('0. 종료')

while True:
    show_menu()
    choice = input('원하는 작업을 선택:')

    if choice=='0':
        print('프로그램을 종료합니다.')
        break
    elif choice in['1','2','3','4']:
        a=float(input('첫번째 숫자를 입력:'))
        b=float(input('두번째 숫자를 입력:'))

        if choice == '1':
            print('결과:',add(a,b))
        elif choice == '2':
            print('결과:',sub(a,b))
        elif choice == '1':
            print('결과:',mul(a,b))
        elif choice == '1':
            print('결과:',div(a,b))
        elif choice == '1':
            print('결과:',cal_bmi(a,b))
        else: print('잘못된 선택입니다.')
