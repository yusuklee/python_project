import requests

API_KEY='1182e540773a5a2f32b1ca1de31b5d64'
CITY = 'Seoul'
URL=f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=kr"


response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    CITY=data['name']
    weather=data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']

    print(f'{CITY}의 날씨 정보')
    print(f'날씨:{weather}')
    print(f'기온:{temp}c 체감온도:{feels_like}c')
    print(f"습도:{humidity}%")
else:
    print('날씨 정보 가져오기 실패')
    print(f'응답 코드: {response.status_code}')
    print(f'응답 메시지: {response.text}')