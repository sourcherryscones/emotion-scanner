import os
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

def process_img(location):
    img = cv2.imread(location)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector=cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    faces = detector.detectMultiScale(gray, 1.1, 4)
    # look into how necessary the bounding-box part is
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    predictions =  DeepFace.analyze(img)
    predictions = predictions[0]
    print("PREDICTIONS ARE:")
    print(predictions)
    final_emotion = predictions['dominant_emotion']
    return final_emotion


@app.route('/storeimg', methods=['POST'])
def store_img():
    img_file = request.files['imgforminput']
    # get file from HTML form
    if img_file.filename == '':
        return '<h1>NO FILE UPLOADED</h1>'
    
    filename = secure_filename(img_file.filename)
    file_loc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img_file.save(file_loc)
    eopt = process_img(file_loc)
    return render_template('output.html', emotion_output=eopt, message=m)
# @app.route("/")
# def hello_world():
#     return 'Hello World!'


@app.route('/')
def index():
    ## /Users/pragya/Desktop/emotionScanner/templates
    return render_template('file_upload.html')







# other stuff from last time >> 

# import os 
# from flask import Flask, render_template, request, redirect, send_file,url_for
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return 'Hello World!'


