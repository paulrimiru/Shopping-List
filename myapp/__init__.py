""" inintialize the app """

from flask import Flask
APP = Flask(__name__, instance_relative_config=True)

@APP.route('/')
def index():
    return 'Index page'

@APP.route('/hello')
def hello():
    return 'Hello World'
if __name__ == '__main__':
    APP.run(debug=True)
