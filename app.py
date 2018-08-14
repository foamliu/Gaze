from flask import Flask
from flask_uploads import UploadSet, ALL, configure_uploads
from settings import *
from datetime import timedelta


app = Flask(__name__)

# configure debug
# app.debug = DEBUG

# configure upload set
app.config['UPLOADED_PACKAGE_DEST'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

packages = UploadSet('PACKAGE', extensions="gaz")
configure_uploads(app, packages)


# import router view
from router import *
if __name__ == '__main__':
    app.run(port=5001, threaded=True, debug=True, host=('0.0.0.0'))
