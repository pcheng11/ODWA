from flask import Blueprint, request, session, url_for, render_template, redirect, flash, session
from flask_login import login_required, current_user, login_user, logout_user
from ..models import Photo
from src import s3, db
import boto3
from config.config import IMAGE_URL_PREFIX
from werkzeug.security import generate_password_hash, check_password_hash
from yolo.detect import detect
import copy
import cv2
import io
import numpy as np
from PIL import Image
upload_blueprint = Blueprint('upload', __name__)

@upload_blueprint.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    print(Photo.query.all())
    success = False
    pic_path = IMAGE_URL_PREFIX
    detected_pic_path = IMAGE_URL_PREFIX
    thumbnail_pic_path = IMAGE_URL_PREFIX
    if request.method == 'POST':
        file = request.files['myfile']
        content = file.read()


        picname = 'user-' + str(current_user.id) + '-' + file.filename
        detected_picname = 'detected-' + picname
        thumbnail_picname = 'thumbnail-' + picname
        print(thumbnail_picname)
        pic_path += picname
        detected_pic_path += detected_picname
        thumbnail_pic_path += thumbnail_picname
        ext = picname[picname.rfind('.'):]

        detected_img = detect(content, ext)
        thumnail_img = to_thumbnail(file)
        # save to sql db
        existing_photo = Photo.query.filter_by(picname=picname).first()
        if not existing_photo:
            photo = Photo(userid=current_user.id,
                        picname=picname,
                        detected_picname=detected_picname,
                        thumbname=thumbnail_picname)
            db.session.add(photo)
            db.session.commit()

        # save to s3
        s3.Bucket('odwa').put_object(Key=picname, Body=content)
        s3.Bucket('odwa').put_object(Key=detected_picname, Body=detected_img)
        s3.Bucket('odwa').put_object(Key=thumbnail_picname, Body=thumnail_img)
        success = True
        
    return render_template('upload.html', success=success, pic1=pic_path, pic2=detected_pic_path)


def to_thumbnail(file):
    image_file = Image.open(file)
    image_file.thumbnail((200, 200), Image.NEAREST)
    buf = io.BytesIO()
    try:
        image_file.save(buf, 'JPEG')
    except:
        image_file.save(buf, 'PNG')
    byte_im = buf.getvalue()
    return byte_im