from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
	return render_template("main.html")

@app.route("/submit")
def submit():
	return render_template("submit.html")

@app.route("/list")
def list():
	return render_template("list.html")
if __name__ == "__main__":

	app.run(debug=True)


