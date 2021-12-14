from flask import Flask, render_template, redirect, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/start', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

app.run()