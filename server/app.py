import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


# SQLite DB 구축

# __file__: the file this module was loaded from
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 추가적인 메모리를 요하므로 꺼둔다.

db = SQLAlchemy(app)
migrate = Migrate(app, db) # Migrate 객체 생성


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# 동적 라우팅
@app.route('/ping/<name>', methods=['GET'])
def ping_pong_name(name):
    print(request)
    return jsonify('User: {}'.format(name))
