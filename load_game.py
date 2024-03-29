from flask import Flask
from views import views


def main():
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix='/')
    app.run(host='0.0.0.0', port=81)


if __name__ == "__main__":
    main()
