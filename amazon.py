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


def amazon(word):
    #*Amazonのurlを取得
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

    print("検索完了")

    #検索結果一覧のurlを取得し、beautiful soupのrequestsで価格をまとめて取得
    from bs4 import BeautifulSoup

    #検索結果のurlを取得し、きれいに抽出
    page_source=driver.page_source
    html_amazon=BeautifulSoup(page_source,"lxml")

    print("検索結果の表示完了")

    #商品名、価格、送料、ポイント,検索結果のurlを表示
    product_name_amazon=html_amazon.find(class_="a-size-base-plus a-color-base a-text-normal")
    price_amazon=html_amazon.find(class_="a-price-whole")
    shipping_fee_amazon=html_amazon.find(class_="a-row a-size-base a-color-secondary s-align-children-center")
    point_amazon=html_amazon.find(class_="a-size-base a-color-price")
    url_amazon=driver.current_url

    #リスト化、カンマを取り除いて見やすくする
    list_amazon=["【"+product_name_amazon.text+"】","￥"+price_amazon.text,shipping_fee_amazon.contents[1].text,point_amazon.text,url_amazon]

    print("Amazon_スクレイピング完了")
    return list_amazon
