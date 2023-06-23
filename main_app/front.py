from flask import Flask,render_template,url_for, request,flash,redirect,session
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import sys
from backend.Uploader.parser import ResumeParser
import os
import backend.openapi as aapi

aapi.__init__()


UPLOAD_FOLDER = '../Resumes'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")

def index(name=None):
    url_for('static', filename='grayscale.js')
    return render_template("index.html",name=name)


@app.route("/FindJobs")
def findjobs():
    return render_template("Find Jobs.html")

@app.route("/uploader", methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            a = ResumeParser(file.filename)
            print(a.get_info())


            return a.get_info()

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    
    app.run(host='0.0.0.0',port=5000)

