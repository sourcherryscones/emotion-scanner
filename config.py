import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ALLOWED_EXTENSIONS={"png","jpeg", "jpg"}
    UPLOAD_FOLDER='./img_storage'
