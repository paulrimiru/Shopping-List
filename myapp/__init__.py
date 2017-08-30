""" inintialize the app """

from flask import Flask
APP = Flask(__name__, instance_relative_config=True)

from myapp import views

if __name__ == '__main__':
    APP.run()
