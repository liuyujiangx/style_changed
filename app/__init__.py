from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

app = Flask(__name__)
api = Api(app)
import os

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:1914571065lyj@localhost:3306/zishi'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

app.config["SECRET_KEY"] = '235c749859ec44c2bd6064ec6da7b927'
UPLOADED_PHOTOS_DEST = './images/'  # 相对路径下的文件夹images
UPLOADED_PHOTO_ALLOW = IMAGES		# 限制只能够上传图片
app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprint


app.register_blueprint(home_blueprint)