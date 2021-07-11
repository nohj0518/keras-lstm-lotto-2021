from flask import Flask, render_template, request, redirect, send_file
from scrapping import get_csv
from keras_lstm_lotto_968_ipynb import get_list_num


app = Flask("SuperScrapper")


@app.route("/")  # @는 데코레이터 /는 root
def home():  # 바로 아래 있는 함수를 찾아 실행해줌
    return render_template("home.html")
    # 그래서 함수 이름이 potato라도 괜찮음
    # 중요한건 데코레이터는 바로 아래 함수가 아닌 것이 오면 syntax error띄움
    # 함수만 정의해 줘야 뭘 실행 시켜줌!


@app.route("/report")
def report():
    numbers = get_list_num()
    return render_template("report.html", numbers=numbers)


app.run()
