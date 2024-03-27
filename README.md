## ネットショップのスクレイピングアプリ
### 概要・サイトURL

　・Amazonや楽天市場、PayPayフリマなどのショッピングサイトの情報をスクレイピング

　・商品名・価格・送料・商品URLを表に一覧化する

　・価格順・ポイント順に並び替える機能

　・直近1か月・3か月・1年・2年の価格推移を表示する機能

URL: https://scrapingapp-3b15c3abeea4.herokuapp.com/



## 使用技術
### 言語系

<img src="https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat"> <img src="https://img.shields.io/badge/-HTML5-333.svg?logo=html5&style=flat"> <img src="https://img.shields.io/badge/-CSS3-1572B6.svg?logo=css3&style=flat"> <img src="https://img.shields.io/badge/Javascript-276DC3.svg?logo=javascript&style=flat">

### フレームワーク

<img src="https://img.shields.io/badge/-Flask-000000.svg?logo=flask&style=flat">

### インフラ

<img src="https://img.shields.io/badge/-Heroku-430098.svg?logo=heroku&style=plastic">



## 製作期間・動機
4か月(2023年10月~2024年1月)

大学のコンピュータ科学基礎という授業で、グループで1つの成果物を作ることになったため。

スクレイピングにはPythonが向いていることを知り、paizaや書籍を使って0から独学を始めた。今回はWebアプリを作成したかったため、並行してHTML,CSS,Flaskの勉強もした。デプロイ時にはHeroku(学割で2年間無償)やGitHubの使い方も学んだ。


## ユースケース図
![スクリーンショット (978)](https://github.com/Hiromu1612/scraping_test/assets/150511546/dd41650f-04f4-40a6-8d2a-ff4dd56195aa)


## 動作画面
### トップページ

　・スクレイピングしたいサイトを選択

　・中央下のアイコンから各サイトにアクセス

 ※検索は40秒ほどかかる

![スクリーンショット (977)](https://github.com/Hiromu1612/scraping_test/assets/150511546/b868fbae-3055-4793-9998-e32fe5e7689b)

・左上のハンバーガーメニューから各ショッピングサイトにアクセス

![スクリーンショット (976)](https://github.com/Hiromu1612/scraping_test/assets/150511546/873401f6-6ebe-4a77-b2fa-def2de5facc4)


### スクレイピング結果ページ
　・価格、ポイントを押すと昇順・降順の切り替え

　・スクレイピングした商品のURLにアクセス

　・直近 1か月・3か月・1年・2年の価格推移を動的に表示(価格.comの価格推移をスクリーンショット)

![スクリーンショット (974)](https://github.com/Hiromu1612/scraping_test/assets/150511546/611b2d36-57ec-45b6-a0a0-3272ae25ffb3)

## 課題
並列処理などで処理速度を改善したものの、ヨドバシカメラと価格コムはサイト自体の動作が遅く、スクレイピングに20秒ほど多くかかってしまう。
そのため、レスポンスが遅く(私のPC上では動作するが)、結果画面まで遷移しない。


## 参考になったもの
 ・paizaラーニング Python入門編, Flask入門編

 ・Python2年生 スクレイピングのしくみ
