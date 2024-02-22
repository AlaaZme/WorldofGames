from flask import Flask
from views import views

def __main__():
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix='/')



    app.run(port=81)

__main__()