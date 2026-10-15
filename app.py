from flask import Flask  # type: ignore[import-not-found]
from flask import render_template # type: ignore[import-not-found]
from flask import url_for # type: ignore[import-not-found]

app = Flask(__name__)

@app.route('/')
def hello_world():
    content = '<h1>Hello World!</h1>'
    content += '<p><a href="' + url_for('jap') + '">Visit JAP</a></p>'
    return content


@app.route('/jap')
@app.route('/jap/')
@app.route('/jap/<model>')
def jap(model=None):
    return render_template('jap/index.html', model=model)

@app.route('/norton/')
def norton():
    return render_template('norton/index.html')

