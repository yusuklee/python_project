import requests

def get_exchange_rate(base:str, target:str):
   
    try:
        url = f"https://open.er-api.com/v6/latest/{base.upper()}" #base에따라서 애초에 환율이 다르게나옴
        response = requests.get(url)
        response.raise_for_status() #요청 실패시 예외 발생
        data = response.json()
        
        return data['rates'][target.upper()] #환율리턴
    except requests.exceptions.RequestException as e:
        print(f'[오류] API 요청 실패:{e}')
        return None
    except KeyError:
        print(f'[오류] 잘못된 통화 코드: {base}->{target}')
        return None
    
def convert_currency(amount:float, rate:float):
    return round(amount *rate, 2)

def main():
    print('환율 변환기(실시간)')
    base=input('기준 통화 (예:USD):').strip()
    target = input('변환할 통화 (예: KRW):').strip()
    try:
        amount = float(input('금액:'))
    except ValueError:
        print('숫자를 입력하세요.')
        return
    
    rate = get_exchange_rate(base,target)
    if rate is None:
        return
    
    converted = convert_currency(amount,rate)
    print(f"\n🌍 {amount} {base.upper()} → {converted} {target.upper()} (환율: {rate:.4f})")

if __name__ == "__main__":
    main()