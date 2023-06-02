from flask import Flask, render_template


app = Flask(__name__)


@app.route("/search")
def home():
    return render_template('search.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5008, debug=True)