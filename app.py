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


@app.route('/scraping', methods=["GET","POST"])
def do_scraping():
    import amazon
    import rakutenn
    import PayPayhurima
    import kakakucom
    word=request.form["search_word"]

    list_amazon = amazon.amazon(word)
    list_rakutenn = rakutenn.rakutenn(word)
    list_PayPayhurima = PayPayhurima.PayPayhurima(word)
    list_kakakucom = kakakucom.kakakucom(word)

    return render_template('result.html',word=word,list_amazon=list_amazon,list_rakutenn=list_rakutenn,list_PayPayhurima=list_PayPayhurima,list_kakakucom=list_kakakucom)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)