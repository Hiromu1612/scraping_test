from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
#直接コードで呼び出さないためグレー表示
import chromedriver_binary

options=Options()
#optionsの引数に加え、ヘッドレスモードに変え、ブラウザを立ち上げずに実行
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

#暗黙的な待機
driver.implicitly_wait(10)

def rakutenn(word):
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
    point_rakutenn=html_rakutenn.find(class_="points--AHzKn")
    time.sleep(3)
    url_rakutenn=driver.current_url

    #円が邪魔だから消す
    html_rakutenn.find(class_="main-price-unit--1Zd3l main-price-unit-grid--upFyx").decompose()

    #リスト化、カンマを取り除いて見やすくする 
    list_rakutenn=["【"+product_name_rakutenn.text+"】","￥"+price_rakutenn.text,shipping_fee_rakutenn.text,point_rakutenn.text,url_rakutenn]

    print("楽天_スクレイピング完了")

    return list_rakutenn