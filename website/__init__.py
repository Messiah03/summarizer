from flask import Flask, redirect

def create_app():   
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'moshe'
    print('hello')
    return app




