from flask import Flask, render_template, jsonify, request,flash,redirect,url_for
from database import get_jobs_from_db,get_job_by_id
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/workspaces/codespaces-flask-v2/resume/'
ALLOWED_EXTENSIONS = {'pdf'}


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ALLOWED_EXTENSIONS

jobs = get_jobs_from_db() # get jobs from database

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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

@app.route("/job/<job_id>/apply", methods = ['POST', 'GET'])
def apply_job(job_id):
    if request.method == 'POST':
        First_Name = request.form['First_Name']
        Last_Name = request.form['Last_Name']
        Email_Id = request.form['Email_Id']
        Linkdin_Link = request.form['Linkdin_Link']
        Github_Link = request.form['Github_Link']
        About = request.form['About']

        if 'Resume' not in request.files:
            flash('No file part')
        file = request.files['Resume']
        
        if file.filename == '':
            flash('No selected file')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],job_id+filename))
            return jsonify([First_Name,Last_Name,Email_Id,Linkdin_Link,Github_Link,About,filename])
        

    #     if 'Resume' in request.files:
    #         file = request.files['Resume']
    #         filenname = secure_filename(file.filename)
    #         file.save(os.path.join(UPLOAD_FOLDER, job_id+ filenname))
    #         return jsonify([First_Name,Last_Name,Email_Id,Linkdin_Link,Github_Link,About,filenname])
    #     else:
    #         return  flash('No file part')
        
    return 'not in post',404

    # data = request.args
    # return jsonify(data)
    

if __name__ == "__main__":
    app.run(debug=True)
