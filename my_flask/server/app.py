from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def invest_calculator():
    title = "Investment Calculator"
    return render_template("index.html", title = title) 


@app.route('/form', methods=["POST"])
def form():
    income = request.form.get("income") #int(input("Enter Income"))
    expense = request.form.get("expenses") #int(input("Enter Expence"))
    principal = request.form.get("principal")
    percent_income = 0 
    if request.method == 'POST':
        if request.form['percent_income'] == '7':
            percent_income = 7
        elif request.form['percent_income'] == '10':
            percent_income = 10
        else:
            percent_income = 12 
            
    yearly_contribution = percent_income * (income - 12 * expense)
    rate_of_interest = 0
    if request.method == 'POST':
        if request.form['apr'] == '7':
            rate_of_interest = 7
        elif request.form['apr'] == '10':
            rate_of_interest = 10
        else:
            rate_of_interest = 20
    increment = 0
    principal = 0


    accumulated_value = 0
    years = []
    yearly_earning = []
    for i in range(0, 21):
        accumulated_value += (principal+(increment * yearly_contribution))*((1+(rate_of_interest/12))**(12*1))
        yearly_earning.append(accumulated_value) 
        yearlys.append(i) 
    
    outputs = zip(years, yearly_earning) 
    ouput_length = len(output)
    
    return render_template("calculation.html", len = len(outputs), calculations = outputs)

    