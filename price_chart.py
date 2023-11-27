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


def price_chart(word):
    #*Amazon価格推移のurlを取得
    print("Amazon価格推移_スクレイピング開始")
    driver.get("https://keepa.com/")

    #暗黙的な待機
    driver.implicitly_wait(100)


    #検索メニューのタグを取得、クリック
    text_menu=driver.find_element_by_id("menuSearch")
    text_menu.click()

    #検索欄のタグを取得、keywordと入力
    text_box=driver.find_element_by_id("searchInput")
    text_box.send_keys(word)

    #検索ボタンのタグを取得、クリック
    btn=driver.find_element_by_id("submitSearch")
    btn.click()

    print("Amazon価格推移_検索完了")

    #暗黙的な待機
    driver.implicitly_wait(10)
    time.sleep(3)


    from bs4 import BeautifulSoup
    #hrefをurlに変換する(相対urlを絶対urlに変換するライブラリ)
    import urllib

    #検索結果のurlを取得し、きれいに抽出
    page_source=driver.page_source
    html_keepa=BeautifulSoup(page_source,"lxml")

    #検索結果のurlを取得
    current_url=driver.current_url

    #検索結果の一番上の商品をクリック 結構大変で複雑になった
    related=html_keepa.find(class_="ag-center-cols-clipper")
    elem=related.find("a")
    href_keepa=elem.get("href")
    url_keepa=urllib.parse.urljoin(current_url,href_keepa)
    driver.get(url_keepa)

    #直近３か月間の価格推移のグラフを表示するタグを取得、クリック
    btn=driver.find_element_by_id("shareChart")
    btn.click()

    #価格推移のグラフのurlを取得、表示
    chart_url=driver.find_element_by_css_selector("#shareChartOverlay > div > img")
    chart_img_url=chart_url.get_attribute("src")

    print("Amazon価格推移_グラフ取得完了")

    return chart_img_url
