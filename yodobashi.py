from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import re
from webdriver_manager.chrome import ChromeDriverManager
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

    #*ヨドバシカメラのurlを取得
def yodobashi(word):
    print("ヨドバシ_スクレイピング開始")
    driver.get("https://www.yodobashi.com/")

    #検索欄のタグを取得、keywordと入力
    text_box=driver.find_element_by_id("getJsonData")
    text_box.send_keys(word)

    #検索ボタンのタグを取得、クリック
    btn=driver.find_element_by_id("js_keywordSearchBtn")
    btn.click()

    print("ヨドバシ_検索完了")

    #暗黙的な待機
    driver.implicitly_wait(10)

    btn=driver.find_element_by_css_selector("#js_showList")
    btn.click()
    driver.implicitly_wait(10)


    #商品名、価格、送料、ポイント、検索結果のurlを表示
    product_name_yodobashi=driver.find_element_by_css_selector("#listContents > div.sectionVerticalList.js_productList > div:nth-child(1) > div.itemListLine_text > a > p:nth-child(2)")
    price_yodobashi=driver.find_element_by_css_selector("#listContents > div.sectionVerticalList.js_productList > div:nth-child(1) > div.itemListLine_text > div.pInfo.liMt05 > ul > li:nth-child(1) > span.productPrice")
    try:
        shipping_fee_yodobashi=driver.find_element_by_css_selector("#listContents > div.sectionVerticalList.js_productList > div:nth-child(1) > div.itemListLine_text > div.pInfo.liMt05 > ul > li:nth-child(2) > span.red")
    except:
        shipping_fee_yodobashi=driver.find_element_by_css_selector("#listContents > div.sectionVerticalList.js_productList > div:nth-child(1) > div.itemListLine_text > div.pInfo.liMt05 > ul > li:nth-child(2) > span.deliveryInfo > span.orange")
    point=driver.find_element_by_css_selector("#listContents > div.sectionVerticalList.js_productList > div:nth-child(1) > div.itemListLine_text > div.pInfo.liMt05 > ul > li:nth-child(1) > span.orange.ml10")
    point_yodobashi=re.findall("[0-9]+",point.text)
    url_yodobashi=driver.current_url



    #リスト化、カンマを取り除いて見やすくする
    list_yodobashi=["【ヨドバシカメラ】",product_name_yodobashi.text,"￥"+price_yodobashi.text[1:],shipping_fee_yodobashi.text,point_yodobashi[0],url_yodobashi]
    print("ヨドバシカメラ_スクレイピング完了")
    return list_yodobashi