from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route('/')

    def hello():
        return 'Hello, study_flask!!'

    return app