from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
    "id": 1,
    "title": "Job 1",
    "Location": "Location 1",
    "Description": "Description 1",
    "Salary": "Salary 1",
    "Date": "2020-01-01"},
    {
    "id": 2,
    "title": "Job 2",
    "Location": "Location 2",
    "Description": "Description 2",
    "Salary": "Salary 2",
    "Date": "2020-01-02"},
    {
    "id": 3,
    "title": "Job 3",
    "Location": "Location 3",
    "Description": "Description 3",
    "Date": "2020-01-03"},
]

@app.route("/")
def hello_world():
    return render_template("index.html",title='Kamal', jobs=JOBS)

@app.route("/api/jobs")
def get_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)
