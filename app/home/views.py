import json
import os

from app import api, db
from app.models import Z_user, Imgs
from . import home
from flask import request
from flask_restful import Resource, fields, marshal_with

basedir = os.path.abspath(os.path.dirname(__file__))


@home.route('/')
def index():
    return 'hello word!!'


class RegisterForm(Resource):
    def post(self):
        data = request.form
        data = json.dumps(data, ensure_ascii=False)
        data = json.loads(data)
        z_user = Z_user(
            id=data['id'],
            username=data['name']
        )
        db.session.add(z_user)
        db.session.commit()
        return data


api.add_resource(RegisterForm, '/form', endpoint='test1')


class Upload_images(Resource):
    def post(self):
        img = request.files.get('photo')
        img_list = ['img', 'png', 'IMG', 'PNG', 'jpg', 'JPG']
        if img.filename[-3:] in img_list:
            path = basedir + "/images/"
            file_path = path + img.filename
            img.save(file_path)
            imgs = Imgs.query.all()
            url_list = []
            name_list = []
            for i in imgs:
                data_url = i.img_url
                data_name = i.img_name
                url_list.append(data_url)
                name_list.append(data_name)
            if file_path not in url_list:
                imgs = Imgs(
                    img_url=file_path,
                    img_name = img.filename
                )
                db.session.add(imgs)
                db.session.commit()
                a = 'success'
            else:
                a = 'Picture already exists'
        else:
            print('err')
        return a


api.add_resource(Upload_images, '/uploads', endpoint='test2')


class ProfileView(Resource):
    resourse_fields = {
        'id': fields.String(),
        'username': fields.String
    }

    @marshal_with(resourse_fields)
    def get(self, id):
        user = Z_user.query.get(id)
        return user


api.add_resource(ProfileView, '/select/<int:id>', endpoint='test')


class StyleMigration(Resource):
    def get(self):
        get_data = request.get_data()
        print(get_data)
        # 将bytes类型转换为json数据
        get_data = json.loads(get_data)
        print(get_data)
        # num1是原图地址
        # num2是模型
        num1 = get_data.get('num1')
        num2 = get_data.get('num2')
        num1 = int(num1)
        num2 = int(num2)
        num1 = num1 - 1
        model_src = 'C:/Users/19145/Desktop/学习/实训/风格迁移/fast-neural-style-tensorflow-master/model/'  # 模型地址
        model_list = os.listdir(model_src)  # 模型名称
        model_file = model_src + model_list[num2]
        imgs = Imgs.query.all()
        url_list = []
        name_list = []
        for i in imgs:
            data_url = i.img_url
            data_name = i.img_name
            url_list.append(data_url)
            name_list.append(data_name)
        image_file = url_list[num1]  # 原图地址
        name = str(num1) + '-' + name_list[num1]
        image_name = name  # 风格图名字ed
        imaged_file = 'C:\\Users\\19145\\Desktop\\文件\\图片/style/'  # 图片保存地址
        cmd = 'python C:/Users/19145/Desktop/学习/实训/风格迁移/fast-neural-style-tensorflow-master\\eval.py --model_file ' + model_file + ' --image_file ' + image_file + ' --image_name ' + image_name + ' --imaged_file ' + imaged_file
        os.system(cmd)
        return 'success'

#x(0:6)
api.add_resource(StyleMigration, '/change/', endpoint='test3')
