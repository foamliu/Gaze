from app import app, packages
from flask import render_template, request, redirect, url_for
from database import insert_package, query_packages, delete_package, insert_deploy
from os import remove
from shutil import copy
from settings import UPLOAD_FOLDER, CURRENT_FOLDER
import docker

logger = app.logger


@app.route('/')
def index():
    return redirect(url_for('show_dashboard'))


@app.route('/upload', methods=['GET', 'POST'])
def show_upload():
    return render_template('upload.html')


@app.route('/upload/submit', methods=['POST'])
def upload_package():
    if request.method == 'POST' and 'file' in request.files:
        package_file = request.files['file']
        package_name = request.form['name']
        description = request.form['description']
        package_true_name = packages.save(package_file, name=package_name+'.gaz')
        print(package_true_name)
        insert_package(user_name="admin", package_name=package_name, description=description)
        return redirect(url_for('show_upload'))

    return redirect(url_for('show_upload'))


@app.route('/dashboard', methods=['GET', 'POST'])
def show_dashboard():
    # cinsert_package(user_name="admin", package_name="test", description="test")
    all_packages = query_packages()
    all_package_info = []
    for package in all_packages:
        package_info = [package["user_name"], package["package_name"], package["description"], "2018-8-7"]
        all_package_info.append(package_info)
    return render_template('dashboard.html', package_list=all_package_info)


@app.route('/dashboard/deploy/<package_name>', methods=['GET', 'POST'])
def dashboard_deploy(package_name):
    insert_deploy(user_name="admin", package_name=package_name)
    package_dir = UPLOAD_FOLDER + "/" + package_name + '.gaz'
    print("deploy the package: " + package_dir)
    copy(package_dir, CURRENT_FOLDER + "/temp/pkg.zip")
    client = docker.from_env()
    result = client.images.build(path=CURRENT_FOLDER, tag="gaze:0.0.1")
    print(result)
    return redirect(url_for('show_dashboard'))


@app.route('/dashboard/delete/<package_name>', methods=['GET', 'POST'])
def dashboard_delete(package_name):
    delete_package(package_name)
    remove(UPLOAD_FOLDER + "/" + package_name + '.gaz')
    return redirect(url_for('show_dashboard'))
