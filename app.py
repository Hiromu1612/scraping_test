from flask import Flask, render_template,request
import amazon
import rakutenn
import PayPayhurima
import price_chart


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scraping', methods=["GET","POST"])
def do_scraping():

    word=request.form["search_word"]

    list_amazon=amazon.amazon(word)
    list_rakutenn=rakutenn.rakutenn(word)
    list_PayPayhurima=PayPayhurima.PayPayhurima(word)
    #chart_img_url=price_chart.price_chart(word)

    return render_template('result.html',word=word,list_amazon=list_amazon,list_rakutenn=list_rakutenn,list_PayPayhurima=list_PayPayhurima)

if __name__ == "__main__":
    app.run(debug=True,port=5001)