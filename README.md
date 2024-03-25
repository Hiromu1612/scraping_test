## Online shop scraping app
### Overview/Site URL
 
・Scraping information from shopping sites such as Amazon, Rakuten Market, PayPay Flea Market, etc.

・List product name, price, shipping fee, and product URL in a table

・Function to sort by price and points

・Function to display price trends for the last 1 month, 3 months, 1 year, and 2 years

URL: https://scrapingapp-3b15c3abeea4.herokuapp.com/



## Technology used
### Language

<img src="https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat"> <img src="https://img.shields.io/badge/-HTML5-333.svg?logo=html5&style=flat"> <img src="https://img.shields.io/badge/-CSS3-1572B6.svg?logo=css3&style=flat"> <img src="https://img.shields.io/badge/Javascript-276DC3.svg?logo=javascript&style=flat">

### Framework

<img src="https://img.shields.io/badge/-Flask-000000.svg?logo=flask&style=flat">

### infrastructure

<img src="https://img.shields.io/badge/-Heroku-430098.svg?logo=heroku&style=plastic">



## Production period/motive
4 months (October 2023 to January 2024)

In a university class called Basics of Computer Science, we were required to create a product as a group.

I learned that Python was suitable for scraping, so I started teaching myself from scratch using paiza and books. This time I wanted to create a web application, so I also studied HTML, CSS, and Flask. During deployment, I also learned how to use Heroku (free for 2 years with a student discount) and GitHub.


## Use case diagram
![スクリーンショット (978)](https://github.com/Hiromu1612/scraping_test/assets/150511546/dd41650f-04f4-40a6-8d2a-ff4dd56195aa)


## Operation screen
### top page

・Select the site you want to scrape

・Access each site from the icon at the bottom center

  *Search takes about 40 seconds

![スクリーンショット (977)](https://github.com/Hiromu1612/scraping_test/assets/150511546/b868fbae-3055-4793-9998-e32fe5e7689b)

・Access each shopping site from the hamburger menu on the top left

![スクリーンショット (976)](https://github.com/Hiromu1612/scraping_test/assets/150511546/873401f6-6ebe-4a77-b2fa-def2de5facc4)


### Scraping results page
・Press the price or point to switch between ascending and descending order

・Access the URL of the scraped product

・Dynamically display price trends for the most recent 1 month, 3 months, 1 year, and 2 years (screenshot of price trends on Kakaku.com)

![スクリーンショット (974)](https://github.com/Hiromu1612/scraping_test/assets/150511546/611b2d36-57ec-45b6-a0a0-3272ae25ffb3)

## assignment
Although processing speeds have been improved through parallel processing, the sites of Yodobashi Camera and Kakaku.com are slow, and scraping takes about 20 seconds more.
As a result, the response is slow (although it works on my PC), and it does not move to the results screen.


## Things that were helpful
  ・paiza Learning Python Introduction, Flask Introduction
 
  ・Python 2nd year student How scraping works
