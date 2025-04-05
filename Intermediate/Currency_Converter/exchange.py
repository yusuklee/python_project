import httpx
import asyncio
import matplotlib.pyplot as plt
import os

exchange_cache = {}

async def fetch_rates(base):
    base = base.upper()
    if base in exchange_cache:
        return exchange_cache[base]
    
    url = f"https://open.er-api.com/v6/latest/{base}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()
        exchange_cache[base] = data['rates']
        return data['rates']
    
async def convert_and_get_rates(base, targets,amount):
    rates = await fetch_rates(base)
    result ={}
    for t in targets:
        rate = rates.get(t.upper())
        if rate:
            result[t.upper()] = round(rate*amount,2)
    return result

def generate_chart(base,rates_dict):
    if not rates_dict:
        return
    targets = list(rates_dict.keys())
    values = [rates_dict[t] for t in targets]

    plt.figure(figsize=(8,4))
    plt.bar(targets,values)
    plt.title(f'{base.upper()} 기준 환율 변환 결과')
    plt.ylabel('금액')
    plt.tight_layout()

    chart_path=os.path.join('static', 'chart.png')
    plt.savefig(chart_path)
    plt.close()
    return chart_path