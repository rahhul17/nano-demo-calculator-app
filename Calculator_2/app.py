from flask import Flask, render_template, request

app = Flask(__name__)

# Store the history of calculations
history = []

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        expression = request.form['expression']
        result = eval(expression)  # Evaluate the expression using eval() (Note: Be cautious when using eval())
        history.append({'expression': expression, 'result': result})

    return render_template('calculator.html', history=history)


if __name__ == '__main__':
    app.run(debug=True)