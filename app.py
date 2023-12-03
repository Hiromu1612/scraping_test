from flask import Flask, render_template,request
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @socketio.on('start_scraping')
# def handle_scraping(data):
#     # スクレイピング処理を開始
#     for i in range(100):
#         # スクレイピングの進行状況をクライアントに送信
#         emit('scraping_progress', {'message': "Amazon_スクレイピング完了"})


from concurrent.futures import ThreadPoolExecutor
import amazon
import rakutenn
import PayPayhurima
import kakakucom
from rq import Queue
from worker import conn

q = Queue(connection=conn)

@app.route('/scraping', methods=["GET","POST"])
def do_scraping():
    word=request.form["search_word"]

    with ThreadPoolExecutor() as executor:
        future_amazon = executor.submit(amazon.amazon, word)
        future_rakutenn = executor.submit(rakutenn.rakutenn, word)
        future_PayPayhurima = executor.submit(PayPayhurima.PayPayhurima, word)
        future_kakakucom = executor.submit(kakakucom.kakakucom, word)

        list_amazon = future_amazon.result()
        list_rakutenn = future_rakutenn.result()
        list_PayPayhurima = future_PayPayhurima.result()
        list_kakakucom = future_kakakucom.result()

    return render_template('result.html',word=word,list_amazon=list_amazon,list_rakutenn=list_rakutenn,list_PayPayhurima=list_PayPayhurima,list_kakakucom=list_kakakucom)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)