from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    if request.method == "POST":
        query = request.form.get("query", "")
    return render_template("index.html", user_input=query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
