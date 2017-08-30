""" inintialize the app """

from flask import Flask

MYAPP = Flask(__name__, instance_relative_config=True)

from app import views

if __name__ == '__main__':
    MYAPP.run(debug=True)
