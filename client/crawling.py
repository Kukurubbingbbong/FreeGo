from selenium import webdriver
from bs4 import BeautifulSoup
import random



def find_reciepe(ingredient):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('disable-gpu')
        options.add_argument('lang=ko_KR')
        browser = webdriver.Chrome('./chromedriver',chrome_options=options)
        browser.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})") # 드라이버 언어설정
        browser.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})") #플러그인 개수 변경

        browser.get("https://www.10000recipe.com/recipe/list.html?q=" + ingredient)

        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.select('div.common_sp_thumb > a')
        names = soup.select('div.common_sp_caption > div.common_sp_caption_tit.line2')

        recipe = {}
        for i in range(len(links)):
            title = names[i].get_text()
            link = "https://www.10000recipe.com/" + links[i].get('href')
            recipe[title] = link
        browser.close()
        return recipe
    except Exception as err:
        print("Error Log : [{}]".format(err))
        return 'fail'