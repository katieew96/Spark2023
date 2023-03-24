from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def invest_calculator():
    title = "Investment Calculator"
    return render_template("index.html", title = title) 


@app.route('/form', methods=["POST"])
def form():
    pass