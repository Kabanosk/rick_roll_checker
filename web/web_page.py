from flask import Flask, render_template, redirect, request, url_for

import checker

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/start', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url_input')
        return redirect(url_for('results', url=url))
    return render_template('index.html')


@app.route('/results/<path:url>', methods=['GET', 'POST'])
def results(url):
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('results.html',
                           is_rick_roll=checker.is_rick_roll(url))


app.run()