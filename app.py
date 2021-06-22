from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    context = {}
    return render_template("home.html", context = context)

@app.route("/dashboard")
def dashboard():
    context = {}
    return render_template("dashboard.html", context = context)

@app.route("/workers")
def workers():
    context = {}
    return render_template("workers.html", context = context)

@app.route("/index_workers")
def index_workers():
    context = {}
    return render_template("workers.html", context = context)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
