"""
    app.py
    ~~~~~~

    sputnikus is looking for work. This app serves templates on Heroku and
    others can use it, if they preserve LICENSE

    :copyright: (c) 2012 by Martin 'sputnikus' Putniorz.
    :license: BSD, see LICENSE for details.
"""
import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def czech():
    return render_template('czech.html')


@app.route('/en')
def english():
    return render_template('english.html')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    # app.debug = True
    app.run(host='0.0.0.0', port=port)
