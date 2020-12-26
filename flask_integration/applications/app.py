from flask import Flask, render_template
import tempfile
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#try to make a dynamic URL with variables
#here we assign the value name dynamically so it should create our route
@app.route("/helloname/<name>")
def helloName(name):
    return 'hello ' + name

#we can also have our variable as integer or float
@app.route("/sqrt/<float:number>")
def printFloatSqrt(number):
    return 'square root of the number = ' + str(number**(0.5))

@app.route("/sqrt/<int:number>")
def printIntSqrt(number):
    return 'square root of the number = ' + str(number**(0.5))


if __name__ == "__main__":
    app.run(port=7777,debug=True)