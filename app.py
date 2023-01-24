from flask import Flask
from flask import jsonify
app = Flask(__name__)


def currency_conversion(amount_in_dollars):
    #calculate the resultant currency and store the result (res)
    res = []

    amount_in_Euro = amount_in_dollars * 0.92
    amount_in_Won = amount_in_dollars * 1232.54
    res.append({'Euro': amount_in_Euro, 'Won': amount_in_Won})

    return res


# Hello world route
@app.route('/')
def hello():
    print("I am inside hello world")
    return 'Hello World! Let me convert currency at route: /currency/<amount_in_dollars>'

@app.route('/currency/<amount_in_dollar>')
def changeroute(amount_in_dollar):
    print(f"Make conversion for {amount_in_dollar}")
    amount = f"{amount_in_dollar}"
    result = currency_conversion(float(amount))
    return jsonify(result)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
