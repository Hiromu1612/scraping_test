from flask import Flask, render_template,request
import concurrent.futures

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scraping', methods=["GET","POST"])
def do_scraping():
    import amazon
    import rakutenn
    import PayPayhurima
    import kakakucom
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

if __name__ == "__main__":
    app.run(debug=True,port=5001)