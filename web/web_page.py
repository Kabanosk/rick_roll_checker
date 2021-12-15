from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/start', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url_input')
        return redirect(url_for('results', url=url))
    return render_template('index.html')

@app.route('/results/<path:url>')
def results(url):
    return render_template('results.html', url=url)


app.run()