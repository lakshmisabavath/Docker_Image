from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get("name")
    roll = request.form.get("roll")
    branch = request.form.get("branch")
    return render_template("result.html", name=name, roll=roll, branch=branch)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
