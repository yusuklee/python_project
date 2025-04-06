import httpx
import asyncio
import matplotlib.pyplot as plt
import os

exchange_cache = {}

async def fetch_rates(base): #base를 기준으로 모든나라 환율보냄
    base = base.upper()
    if base in exchange_cache:
        return exchange_cache[base]
    
    url = f"https://open.er-api.com/v6/latest/{base}"
    async with httpx.AsyncClient() as client: #비동기 request 만듬
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()
        exchange_cache[base] = data['rates']
        return data['rates'] 
    
async def convert_and_get_rates(base, targets,amount):
    rates = await fetch_rates(base) #모든나라 환율 data['rates']딕셔너리에 잇음 
    result ={} 
    for t in targets: #targets를 애초에 리스트로 받을 생각
        rate = rates.get(t.upper())
        if rate:
            result[t.upper()] = round(rate*amount,2) 
    return result #예를들어서 usd를 기준으로 하고 krw를 target으로하고 amount 1이면 {'krw':1400}

def generate_chart(base,rates_dict): #result가 rates_dict에 들감
    if not rates_dict:
        return
    targets = list(rates_dict.keys()) #krw, usd 이런게 targets리스트에 저장
    values = [rates_dict[t] for t in targets] #요놈들의 환율이 여기 리스트에 저장

    plt.figure(figsize=(8,4))
    plt.bar(targets,values)
    plt.title(f'Exchange rate conversion result based on {base.upper()} currency')
    plt.ylabel('COST')
    plt.tight_layout() #알아서 깔끔하게 해주는함수 ㅇㅇ

    chart_path=os.path.join('static', 'chart.png')
    plt.savefig(chart_path)
    plt.close()
    return chart_path