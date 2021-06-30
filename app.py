from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.tasks.db'
deb = SQLAlchemy(app)


@app.route('/')
def home():
    return 'Hello word'


if __name__ == '__main__':
    app.run(debug=True)
