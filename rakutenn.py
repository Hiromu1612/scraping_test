from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import re
#直接コードで呼び出さないためグレー表示
import chromedriver_binary

options=Options()
#optionsの引数に加え、ヘッドレスモードに変え、ブラウザを立ち上げずに実行
options.add_argument('--headless')                         
options.add_argument('--disable-gpu')                      
options.add_argument('--disable-extensions')               
options.add_argument('--proxy-server="direct://"')         
options.add_argument('--proxy-bypass-list=*')              
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('--lang=ja')                          
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--log-level=3")
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

#暗黙的な待機
driver.implicitly_wait(10)



def rakutenn(word):
    try:
        #*楽天ショッピングのurlを取得
        print("楽天ショッピング_スクレイピング開始")
        driver.get("https://search.rakuten.co.jp/search/mall?sitem=")

        #検索欄のタグを取得、keywordと入力
        text_box_rakutenn=driver.find_element_by_class_name("ri-cmn-hdr-search-input")
        text_box_rakutenn.send_keys(word)

        #検索ボタンのタグを取得、クリック
        btn=driver.find_element_by_id("ri-cmn-hdr-button")
        btn.click()

        print("楽天_検索完了")

        #検索結果一覧のurlを取得し、beautiful soupのrequestsで価格をまとめて取得
        from bs4 import BeautifulSoup

        #検索結果のurlを取得し、きれいに抽出
        page_source=driver.page_source
        html_rakutenn=BeautifulSoup(page_source,"lxml")

        #商品名、価格、送料、ポイント、検索結果のurlを表示
        product_name_rakutenn=html_rakutenn.find(class_="title-link--3Ho6z")
        price_rakutenn=html_rakutenn.find(class_="price--OX_YW")
        shipping_fee_rakutenn=html_rakutenn.find(class_="free-shipping-label--HpFaT")
        #ポイントだけ抽出、正規表現で数字だけ取り出す
        point=html_rakutenn.find(class_="points--AHzKn")
        point_rakutenn=re.findall("[0-9]+",point.text)
        url_rakutenn=driver.current_url


        #円が邪魔だから消す
        html_rakutenn.find(class_="main-price-unit--1Zd3l main-price-unit-grid--upFyx").decompose()

        #リスト化、カンマを取り除いて見やすくする 
        list_rakutenn=["【楽天ショップ】",product_name_rakutenn.text,"￥"+price_rakutenn.text,shipping_fee_rakutenn.text,point_rakutenn[0],url_rakutenn]

        print("楽天_スクレイピング完了")

    except:
        print("楽天_スクレイピング失敗")
        list_rakutenn=["【楽天ショップ】","-","-","-","-","-"]

    return list_rakutenn