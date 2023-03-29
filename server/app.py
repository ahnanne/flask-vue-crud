import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


# __file__: the file this module was loaded from
# basedir: /Users/an-yein/flask-vue-crud/server
basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# SQLite DB 구축
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

###################### 모델 생성 ######################
# 모델은 DB에 테이블을 설정하는 것과 같다.
class Puppy(db.Model):
    # 클래스 이름을 기반으로 기본 테이블 이름이 제공되지만,
    # 다음과 같이 덮어쓸 수 있다.
    __tablename__ = 'puppies'


    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Puppy {self.name} is {self.age} year/s old"


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# 동적 라우팅
@app.route('/ping/<name>', methods=['GET'])
def ping_pong_name(name):
    print(request)
    return jsonify('User: {}'.format(name))


if __name__ == '__main__':
    app.run()