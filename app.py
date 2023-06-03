from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route('/search')
def search():
    return render_template('search.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5008, debug=True)