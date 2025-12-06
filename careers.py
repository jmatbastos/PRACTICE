import os
from flask import (
    Flask, Blueprint, session, flash, redirect, render_template, request, url_for, send_from_directory
)

from werkzeug.utils import secure_filename

from .db_careers import (
    get_jobs, get_job_categories, get_myapplications, make_application
)

app = Flask(__name__)
app.config.from_mapping(
    # WARNING, MUST CHANGE THIS FOR PRODUCTION !
    UPLOAD_FOLDER='/XAMPP/htdocs/PRACTICE/static/uploads',
    MAX_CONTENT_LENGTH = 100 * 1000,
)

bp = Blueprint('careers', __name__)

@bp.route('/')
def index():
    return render_template('careers/index.html')    

@bp.route('/jobs')
@bp.route('/jobs/<int:id>')
def jobs(id = None):
    pass

@bp.route('/applications')
def applications():
    pass

@bp.route('/apply/<int:id>', methods=('GET', 'POST'))
def apply(id):
    app

@bp.route('/download/<name>')
def download(name):
    if 'user_id' in session:    
        try:
            return send_from_directory(app.config["UPLOAD_FOLDER"], str(session['user_id']) + name )
        except: 
            flash(f"No file exists with name {name}")

        return redirect(url_for('careers.index'))  
    
    return redirect(url_for('auth.login'))
   
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'pdf'}
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

