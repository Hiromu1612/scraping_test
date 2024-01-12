from flask import Flask, render_template,request
<<<<<<< HEAD
import concurrent.futures

app = Flask(__name__)
=======
import os

app = Flask(__name__)

>>>>>>> 16b468ea18514ee9cfc27338c3550816cf9c62d9

@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
=======

# @socketio.on('start_scraping')
# def handle_scraping(data):
#     # スクレイピング処理を開始
#     for i in range(100):
#         # スクレイピングの進行状況をクライアントに送信
#         emit('scraping_progress', {'message': "Amazon_スクレイピング完了"})


>>>>>>> 16b468ea18514ee9cfc27338c3550816cf9c62d9
@app.route('/scraping', methods=["GET","POST"])
def do_scraping():
    import amazon
    import rakutenn
    import PayPayhurima
    import kakakucom
<<<<<<< HEAD
    import yodobashi
    word=request.form["search_word"]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_amazon = executor.submit(amazon.amazon, word)
        future_rakutenn = executor.submit(rakutenn.rakutenn, word)
        future_PayPayhurima = executor.submit(PayPayhurima.PayPayhurima, word)
        future_kakakucom = executor.submit(kakakucom.kakakucom, word)
        future_yodobashi = executor.submit(yodobashi.yodobashi, word)

    for future in concurrent.futures.as_completed([future_amazon, future_rakutenn, future_PayPayhurima, future_kakakucom, future_yodobashi]):
        if future == future_amazon:
            list_amazon = future.result()
        elif future == future_rakutenn:
            list_rakutenn = future.result()
        elif future == future_PayPayhurima:
            list_PayPayhurima = future.result()
        elif future == future_kakakucom:
            list_kakakucom = future.result()
        elif future == future_yodobashi:
            list_yodobashi = future.result()
    return render_template('result.html',word=word,list_amazon=list_amazon,list_rakutenn=list_rakutenn,list_PayPayhurima=list_PayPayhurima,list_kakakucom=list_kakakucom,list_yodobashi=list_yodobashi)
=======
    word=request.form["search_word"]

    list_amazon = amazon.amazon(word)
    list_rakutenn = rakutenn.rakutenn(word)
    list_PayPayhurima = PayPayhurima.PayPayhurima(word)
    list_kakakucom = kakakucom.kakakucom(word)
>>>>>>> 16b468ea18514ee9cfc27338c3550816cf9c62d9

    return render_template('result.html',word=word,list_amazon=list_amazon,list_rakutenn=list_rakutenn,list_PayPayhurima=list_PayPayhurima,list_kakakucom=list_kakakucom)
if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True,port=5001)
=======
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
>>>>>>> 16b468ea18514ee9cfc27338c3550816cf9c62d9
