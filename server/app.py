#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<string:page>")
def print_string(page):
    print(page)
    return page

@app.route("/count/<int:num>")
def count(num):
    numbers = []
    for x in range(num):
        numbers.append(x)
    return numbers

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, num2, operation):
    if operation == '+' :
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return "Operation should be +, -, *, div, or %"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
