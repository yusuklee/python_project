import requests
from bs4 import BeautifulSoup

#섹션 페이지에서 기사 링크 수집
def get_links(url, max_count=10):
    headers = {'User-Agent':'Mozilla/5.0'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    tags = soup.select('a[href*="n.news.naver.com"]')
    links=[]
    for tag in tags:
        href = tag.get('href')
        if href and href.startswith("https://n.news.naver.com"):
            links.append(href)
    return list(set(links))[:max_count]


#2 제목이랑 내용추출
def get_contents(url):
    headers = {'User-Agent':'Mozilla/5.0'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.select_one('strong.sa_text_strong')
    if not title:
        title = soup.select_one('h2.media_end_head_headline')
    content = soup.select_one('article#dic_area') #그기사의 본문이담겨잇는 article태크가 저장됨

    return{
        'url':url,
        'title':title.get_text(strip=True) if title else '제목없음',
        'content':content.get_text(strip=True) if content else '본문없음'
    }


#섹션 선택하기
section_urls = {
    '정치': "https://news.naver.com/section/100",
    '경제': "https://news.naver.com/section/101",
    '사회': "https://news.naver.com/section/102",
    '생활/문화': "https://news.naver.com/section/103",
    '세계': "https://news.naver.com/section/104",
    'IT/과학': "https://news.naver.com/section/105"
}

#메인 함수
def main():
    print("가져올 섹션을 선택하십쇼:")
    for i, name in enumerate(section_urls.keys(),1):
        print(f"{i}.{name}")

    choice = int(input("번호 입력:"))
    section_name = list(section_urls.keys())[choice-1]
    section_url = section_urls[section_name]

    print(f"\n {section_name} 뉴스 영역에서 기사 가져오는중...\n")
    links = get_links(section_url,10)

    for i, link in enumerate(links, 1):
        article = get_contents(link) #article에 딕셔너리로 저장됨
        print(f"{i}. {article['title']}")
        print(f"URL: {article['url']}")
        print(f"본문: {article['content'][:100]}...\n")

if __name__ == "__main__":
    main()