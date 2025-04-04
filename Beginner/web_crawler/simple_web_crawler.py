import requests
from bs4 import BeautifulSoup

def simple_crawler(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # 수정된 선택자
        headlines = soup.select('a[href*="news.naver.com"]')

        print("📰 뉴스 헤드라인:")
        for i, tag in enumerate(headlines[:10], 1):
            title = tag.get_text(strip=True)
            link = tag.get('href')
            if title:
                print(f"{i}. {title} - {link}")

    except Exception as e:
        print(f"오류발생: {e}")

if __name__ == "__main__":
    url = "https://news.naver.com"
    simple_crawler(url)