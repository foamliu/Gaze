from app import app, packages
from flask import render_template, request, redirect, url_for, abort

logger = app.logger


@app.route('/')
def index():
    return redirect(url_for('show_upload'))


@app.route('/upload', methods=['GET', 'POST'])
def show_upload():
    return render_template('upload.html')


@app.route('/upload/submit', methods=['POST'])
def upload_package():
    if request.method == 'POST' and 'file' in request.files:
        package_file = request.files['file']
        package_new_name = request.form['name']
        package_true_name = packages.save(package_file, name=package_new_name+'.gz')
        print(package_true_name)
        return redirect(url_for('show_upload'))

    return redirect(url_for('show_upload'))
