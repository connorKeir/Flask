from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<user_celsius>')
def celsius_to_fahrenheit(user_celsius=0):
    celsius = float(user_celsius)
    fahrenheit = celsius * 9.0 / 5 + 32
    return "User Celsius input: {:.2f} Result: {:.2f} F".format(celsius, fahrenheit)


if __name__ == '__main__':
    app.run()
