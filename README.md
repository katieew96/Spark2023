# Spark2023
### Finance/Education/Health

Team members: Ekta Patelekta, Katie Warren & Joel Montano
Email addresses: patelektae18, warrenk14, montanoj14

We focused on Finance for our project. Decided that since we are all graduating soon, it would be nice to know what we would want to invest monthly from our new jobs after graduation. That was how this little project got born. We just went from there, with figuring out different monthly contributions to invest. Seeing how much of a nest egg different precentages of monthly income would grow for us. How assertive we would want to aim for our initial investments over the next few years to get the best investment rates possible.

We used HTML, CSS, Bootstrap, Flask, Python, JavaScript and GitHub for technologies.

# How to use the index.html file:
All of the code is on the single file. You open it through your browser. Then you add user info of your yearly income, monthly expenses, and what you are planning on investing. Next you click the submit button and a new page will pup up with feedback.

### Calculations used
income = int(input("Enter Income"))
expense = int(input("Enter Expence"))
Principal = 0
yearly_contribution = 0
number_of_years = 0
Rate_of_interest = 0
increament = 0
Accumulated_value = 0


Principal = income - expense

Accumulated_value = (Principal+(increament * yearly_contribution))*((1+ (Rate_of_interest/12))**(12*number_of_years))

print(Accumulated_value)

def investment_function(income, expence, Principal, yearly_contribution, number_of_years, Rate_of_interest, increament):
      print(Accumulated_value)
