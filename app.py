from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    
    return render_template("index.html", nama=None)


@app.route("/hasil", methods=["POST"])
def hasil():
    
    nama = request.form.get("nama", "").strip()
    return render_template("index.html", nama=nama)


if __name__ == "__main__":
    app.run(debug=True)