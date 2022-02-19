from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def is_in_db(user_url):
    urls = db.collection('rickroll').document('urls').get().to_dict()
    for url in urls:
        if url in user_url:
            return True
    return False

app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/start', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url_input')
        return redirect(url_for('results', url=url))
    return render_template('main.html')


@app.route('/results/<path:url>', methods=['GET', 'POST'])
def results(url):
    if request.method == 'POST':
        if request.form.get('back') == 'Check next link!':
            return redirect(url_for('index'))
    return render_template('results.html',
                           is_rick_roll=is_in_db(url))

if __name__ == '__main__':
    app.run()
