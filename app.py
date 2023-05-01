from flask import Flask, render_template, jsonify
from database import get_jobs_from_db,get_job_by_id

app = Flask(__name__)


jobs = get_jobs_from_db() # get jobs from database


@app.route("/")
def hello_world():
    return render_template("index.html",title='Kamal', jobs=jobs)

@app.route("/api/jobs")
def get_jobs():
    return jsonify(jobs)

@app.route("/job/<job_id>")
def get_job(job_id):
    job = get_job_by_id(job_id)
    if not job:
        return 'no jobs',404
    else:
        return render_template("jobpage.html", job=job)

if __name__ == "__main__":
    app.run(debug=True)
