from flask import Flask, render_template, jsonify
from database import get_jobs_from_db


app = Flask(__name__)


jobs = get_jobs_from_db() # get jobs from database


@app.route("/")
def hello_world():
    return render_template("index.html",title='Kamal', jobs=jobs)

@app.route("/api/jobs")
def get_jobs():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True)
