from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
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
driver = webdriver.Chrome(options=options)

#暗黙的な待機
driver.implicitly_wait(10)

#*Amazonのurlを取得
def amazon(word):
    print("Amazon_スクレイピング開始")
    driver.get("https://www.amazon.co.jp/")

    #暗黙的な待機
    driver.implicitly_wait(10)

    #検索欄のタグを取得、keywordと入力
    text_box=driver.find_element_by_id("twotabsearchtextbox")
    text_box.send_keys(word)

    #検索ボタンのタグを取得、クリック
    btn=driver.find_element_by_id("nav-search-submit-button")
    btn.click()

    print("Amazon_検索完了")

    #検索結果一覧のurlを取得し、beautiful soupのrequestsで価格をまとめて取得
    from bs4 import BeautifulSoup

    #検索結果のurlを取得し、きれいに抽出
    page_source=driver.page_source
    html_amazon=BeautifulSoup(page_source,"lxml")

    #商品名、価格、送料、ポイント,検索結果のurlを表示
    product_name_amazon=html_amazon.find(class_="a-size-base-plus a-color-base a-text-normal")
    price_amazon=html_amazon.find(class_="a-price-whole")
    shipping_fee_amazon=html_amazon.find(class_="a-row a-size-base a-color-secondary s-align-children-center")
    #ポイントだけ抽出、正規表現で数字だけ取り出す
    point=html_amazon.find(class_="a-size-base a-color-price")
    point_amazon=re.findall("[0-9]+",point.text)
    url_amazon=driver.current_url

    #リスト化、カンマを取り除いて見やすくする
    list_amazon=["【Amazon】",product_name_amazon.text,"￥"+price_amazon.text,shipping_fee_amazon.contents[1].text,point_amazon[0],url_amazon]

    print("Amazon_スクレイピング完了")
    return list_amazon
