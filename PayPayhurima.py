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

def PayPayhurima(word):
    #*PayPayフリマのurlを取得
    print("PayPayフリマ_スクレイピング開始")
    driver.get("https://paypayfleamarket.yahoo.co.jp/")

    #検索欄のタグを取得、keywordと入力
    text_box=driver.find_element_by_name("word")
    text_box.send_keys(word+" 新品")

    #検索ボタンのタグを取得、クリック
    btn=driver.find_element_by_css_selector(".sc-14dcb79f-4 > img")
    btn.click()

    print("PayPayフリマ_検索完了")

    time.sleep(2)

    #販売中のみ表示ボタンのタグを取得、クリック
    btn=driver.find_element_by_css_selector(".sc-3cadff20-4 > .sc-3cadff20-5 .sc-bfe2724c-2")
    btn.click()

    #一番上に出てきた商品画像のタグを取得、クリック なぜかボタンクリックができなかったため、他の方法でクリック
    btn=driver.find_element_by_css_selector("#itm > a:nth-child(1)")
    btn.click()
    #driver.execute_script("arguments[0].click();",btn)
    time.sleep(6)
    #商品名、価格、送料、ポイント、検索結果のurlを表示
    product_name_PayPayhurima=driver.find_element_by_css_selector("#__next > div > main > div.sc-9bae193f-0.eWnaAG.ItemMain__Component > div.sc-9bae193f-1.bgQUin > aside > div.sc-9d0e932e-1.bnkqvI > div.sc-9d0e932e-2.lgdfyj > div.sc-9d0e932e-7.evNHhY > div.sc-9d0e932e-8.hotNPS > h1 > span")
    price_PayPayhurima=driver.find_element_by_css_selector("#__next > div > main > div.sc-9bae193f-0.eWnaAG.ItemMain__Component > div.sc-9bae193f-1.bgQUin > aside > div.sc-9d0e932e-1.bnkqvI > div.sc-9d0e932e-2.lgdfyj > div.sc-9d0e932e-19.iYAaHs > div > div > span")
    shipping_fee_PayPayhurima=driver.find_element_by_css_selector("#__next > div > main > div.sc-9bae193f-0.eWnaAG.ItemMain__Component > div.sc-9bae193f-1.bgQUin > aside > div.sc-9d0e932e-1.bnkqvI > div.sc-9d0e932e-2.lgdfyj > div.sc-dd0e56c9-0.Bjegt > span")
    point_PayPayhurima="0ポイント"
    url_PayPayhurima=driver.current_url


    #リスト化、カンマを取り除いて見やすくする
    list_PayPayhurima=["【"+product_name_PayPayhurima.text+"】","￥"+price_PayPayhurima.text[:-1],shipping_fee_PayPayhurima.text,point_PayPayhurima,url_PayPayhurima]

    print("PayPayフリマ_スクレイピング完了")
    return list_PayPayhurima
