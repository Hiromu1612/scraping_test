from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
#直接コードで呼び出さないためグレー表示
import chromedriver_binary

options=Options()
#optionsの引数に加え、ヘッドレスモードに変え、ブラウザを立ち上げずに実行
options.add_argument("--headless")                        
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



def PayPayhurima(word):
    try:
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

        #暗黙的な待機
        driver.implicitly_wait(10)

        #販売中のみ表示ボタンのタグを取得、クリック
        btn=driver.find_element_by_css_selector("#__next > div > div.sc-f4bb2e12-0.hZMyZW.Search__SearchContent > div > div > main > div > div > div.sc-f4bb2e12-4.hgsYgw > div.sc-21098eb2-0.kgfgJF > div.sc-21098eb2-3.lgjiKA > div.sc-21098eb2-4.jLvCLZ > div.sc-21098eb2-5.gZoGQD > label > span.sc-e1dc44f2-1.ePzayz > span > input")
        btn.click()


        #一番上に出てきた商品画像のタグを取得、クリック なぜかボタンクリックができなかったため、他の方法でクリック
        btn=driver.find_element_by_css_selector(".sc-fad0d81d-0:nth-child(1) > .sc-fad0d81d-1")
        #暗黙的な待機
        driver.implicitly_wait(10)
        btn.click()
        #driver.execute_script("arguments[0].click();",btn)

        #商品名、価格、送料、ポイント、検索結果のurlを表示
        product_name_PayPayhurima=driver.find_element_by_css_selector("#__next > div > main > div.sc-9bae193f-0.eWnaAG.ItemMain__Component > div.sc-9bae193f-1.bgQUin > aside > div.sc-9d0e932e-1.bnkqvI > div.sc-9d0e932e-2.lgdfyj > div.sc-9d0e932e-7.evNHhY > div.sc-9d0e932e-8.hotNPS > h1 > span")
        price_PayPayhurima=driver.find_element_by_css_selector("#__next > div > main > div.sc-9bae193f-0.eWnaAG.ItemMain__Component > div.sc-9bae193f-1.bgQUin > aside > div.sc-9d0e932e-1.bnkqvI > div.sc-9d0e932e-2.lgdfyj > div.sc-9d0e932e-19.iYAaHs > div > div > span")
        shipping_fee_PayPayhurima=driver.find_element_by_css_selector("#__next > div > main > div.sc-9bae193f-0.eWnaAG.ItemMain__Component > div.sc-9bae193f-1.bgQUin > aside > div.sc-9d0e932e-1.bnkqvI > div.sc-9d0e932e-2.lgdfyj > div.sc-dd0e56c9-0.Bjegt > span")
        point_PayPayhurima="0"
        url_PayPayhurima=driver.current_url


        #リスト化、カンマを取り除いて見やすくする
        list_PayPayhurima=["【PayPayフリマ】",product_name_PayPayhurima.text,"￥"+price_PayPayhurima.text[:-1],shipping_fee_PayPayhurima.text,point_PayPayhurima,url_PayPayhurima]
        print("PayPayフリマ_スクレイピング完了")
    except:
        print("PayPayフリマ_スクレイピング失敗")
        list_PayPayhurima=["【PayPayフリマ】","-","-","-","-","-"]
        
        
    return list_PayPayhurima