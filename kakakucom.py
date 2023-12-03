from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import re
#直接コードで呼び出さないためグレー表示
import chromedriver_binary
import os

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

def kakakucom(word):
    try:
        #*価格コムのurlを取得
        print("価格コム_スクレイピング開始")
        driver.get("https://kakaku.com/")

        #暗黙的な待機
        driver.implicitly_wait(10)

        #検索欄のタグを取得、wordと入力
        text_box=driver.find_element_by_id("query")
        text_box.send_keys(word)

        #暗黙的な待機
        driver.implicitly_wait(10)

        #検索ボタンのタグを取得、クリック
        btn=driver.find_element_by_id("main_search_button")
        btn.click()

        #暗黙的な待機
        driver.implicitly_wait(10)

        print("価格コム_検索完了")

        #一番上に出てきた商品画像のタグを取得、クリック 
        btn=driver.find_element_by_class_name("p-result_item_btn")
        btn.click()

        #暗黙的な待機
        driver.implicitly_wait(10)

        #商品名、価格、送料、ポイント、検索結果のurlを表示
        product_name_kakakucom=driver.find_element_by_class_name("boxL")
        try:
            price_kakakucom=driver.find_element_by_css_selector("#mainLeft > table > tbody > tr:nth-child(2) > td.alignR > p.fontPrice")
        except:
            price_kakakucom=driver.find_element_by_css_selector("#mainLeft > table > tbody > tr:nth-child(3) > td.p-priceTable_col.p-priceTable_col-priceBG > div > p.p-PTPrice_price")
        try:
            shipping_fee_kakakucom=driver.find_element_by_css_selector("#mainLeft > table > tbody > tr:nth-child(2) > td:nth-child(3) > font")
        except:
            shipping_fee_kakakucom=driver.find_element_by_css_selector("#mainLeft > table > tbody > tr:nth-child(3) > td.p-priceTable_col.p-priceTable_col-shipping > p")
        #ポイントがない場合は0を返す
        try:
            point=driver.find_element_by_css_selector("#mainLeft > table > tbody > tr:nth-child(3) > td.p-priceTable_col.p-priceTable_col-priceBG > div > p.p-PTPoint > span.p-PTPoint_num")
            point_kakakucom=re.findall("[0-9]+",point.text)
            if not point_kakakucom:
                point_kakakucom = "0"
            else:
                point_kakakucom = point_kakakucom[0]

        except:
            point_kakakucom="0"
        url_kakakucom=driver.current_url


        #リスト化、カンマを取り除いて見やすくする
        list_kakakucom=["【価格コム】",product_name_kakakucom.text,price_kakakucom.text,shipping_fee_kakakucom.text,point_kakakucom,url_kakakucom]
        print("価格コム_スクレイピング完了")

    except:
        print("価格コム_スクレイピング失敗")
        list_kakakucom=["【価格コム】","-","-","-","-","-"]


    #*価格推移を表示
    print("価格コム_価格推移取得開始")
    directory=r"C:\Users\1612h\.vscode\.vscode\scrap\static"
    try:
        btn=driver.find_element_by_class_name("priceRateLink")
        btn.click()
        #暗黙的な待機
        driver.implicitly_wait(10)
        url=driver.current_url
        #末尾のurlを取得
        last_url=url.split("/")[-1]
        #末尾のurlを価格推移のurlに変更
        url_kakakucom = driver.current_url.replace(last_url, "pricehistory/")
        driver.get(url_kakakucom)



        #3ヶ月の価格推移を表示
        driver.find_element_by_css_selector("#main > div.box09.mTop10 > div").screenshot_as_png

        with open(os.path.join(directory, 'price_chart_3month.png'), 'wb') as f:
            f.write(driver.find_element_by_css_selector("#main > div.box09.mTop10 > div").screenshot_as_png)


        #1か月の価格推移を表示
        driver.find_element_by_css_selector(".amChartsButton:nth-child(1)").click()
        driver.find_element_by_css_selector("#main > div.box09.mTop10 > div").screenshot_as_png

        with open(os.path.join(directory, 'price_chart_1month.png'), 'wb') as f:
            f.write(driver.find_element_by_css_selector("#main > div.box09.mTop10 > div").screenshot_as_png)

        #1年の価格推移を表示
        driver.find_element_by_css_selector(".amChartsButton:nth-child(3)").click()
        driver.find_element_by_css_selector("#main > div.box09.mTop10 > div").screenshot_as_png

        with open(os.path.join(directory, 'price_chart_1year.png'), 'wb') as f:
            f.write(driver.find_element_by_css_selector("#main > div.box09.mTop10 > div").screenshot_as_png)

        #2年の価格推移を表示
        driver.find_element_by_css_selector(".amChartsButton:nth-child(4)").click()
        driver.find_element_by_css_selector("#main > div.box09.mTop10 > div").screenshot_as_png

        with open(os.path.join(directory, 'price_chart_2year.png'), 'wb') as f:
            f.write(driver.find_element_by_css_selector("#main > div.box09.mTop10 > div").screenshot_as_png)



        print("価格コム_価格推移取得完了")
    except:
        print("価格コム_価格推移取得失敗")
        
    return list_kakakucom