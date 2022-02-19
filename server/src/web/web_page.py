from flask import Flask, render_template, redirect, request, url_for

import checker
from checker import is_rick_roll

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
        if request.form.get('back') == 'Check another link!':
            return redirect(url_for('index'))
        if request.form.get('email1') is not None:
            db = checker.db
            new_email = request.form.get('email')
            emails = db.collection('users').document('emails').get().to_dict()
            last_id = int(list(emails.keys())[-1])
            emails[str(last_id+1)] = new_email
            db.collection('users').document('emails').set(emails)
            return redirect(url_for('thanks'))
    return render_template('results.html',
                           is_rick_roll=is_rick_roll(url))

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('thanks.html')

app.run()
