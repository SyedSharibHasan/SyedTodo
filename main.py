from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/harry")
def harry():
    return "Hello harry bhai4!"
app.run(debug=True)





