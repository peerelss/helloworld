from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_run():
    return 'Welcome to My Watchlist!'
