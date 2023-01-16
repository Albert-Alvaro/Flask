from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<name>')
def f(name=""):
    return f"{name} Celsius is converted to {convert_celsius_fahrenheit(float(name))} Fahrenheit"


def convert_celsius_fahrenheit(celsius):
    """This function is for converting celsius value into fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit




if __name__ == '__main__':
    app.run()


