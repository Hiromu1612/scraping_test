from flask import Flask, render_template,request
import concurrent.futures
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('start_scraping')
def handle_scraping(data):
    # スクレイピング処理を開始
    for i in range(100):
        # スクレイピングの進行状況をクライアントに送信
        emit('scraping_progress', {'message': "Amazon_スクレイピング完了"})


@app.route('/scraping', methods=["GET","POST"])
def do_scraping():
    import amazon
    import rakutenn
    import PayPayhurima
    import kakakucom
    import logging
    word=request.form["search_word"]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_amazon = executor.submit(amazon.amazon, word)
        future_rakutenn = executor.submit(rakutenn.rakutenn, word)
        future_PayPayhurima = executor.submit(PayPayhurima.PayPayhurima, word)
        future_kakakucom = executor.submit(kakakucom.kakakucom, word)

    for future in concurrent.futures.as_completed([future_amazon, future_rakutenn, future_PayPayhurima, future_kakakucom]):
        if future == future_amazon:
            list_amazon = future.result()
            logging.info(f'Amazon: {list_amazon}')  # ログ出力
        elif future == future_rakutenn:
            list_rakutenn = future.result()
            logging.info(f'rakutenn: {list_rakutenn}')  # ログ出力
        elif future == future_PayPayhurima:
            list_PayPayhurima = future.result()
            logging.info(f'PayPay: {list_PayPayhurima}')  # ログ出力
        elif future == future_kakakucom:
            list_kakakucom = future.result()
            logging.info(f'kakakucom: {list_kakakucom}')  # ログ出力

    # ログファイルの内容を読み取る
    with open('app.log', 'r') as f:
        logs = f.read()

    return render_template('result.html',word=word,list_amazon=list_amazon,list_rakutenn=list_rakutenn,list_PayPayhurima=list_PayPayhurima,list_kakakucom=list_kakakucom,logs=logs)

if __name__ == "__main__":
    app.run(debug=True,port=5000)