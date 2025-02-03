from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def index():
    username = os.getenv('USER')
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    return f'<h1>Mi primera APP Flask deployeada en render.<br>{username}<br>{email}<br>{password}</h1>'


def status_404(error):
    return '<h1>PÁGINA NO ENCONTRADA.</h1>'


if __name__ == '__main__':
    app.register_error_handler(404, status_404)
    app.run(debug=True)