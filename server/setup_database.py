import os
from app import app
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

app_ctx = app.app_context()
app_ctx.push()

# __file__: the file this module was loaded from
# basedir: /Users/an-yein/flask-vue-crud/server
basedir = os.path.abspath(os.path.dirname(__file__))


# SQLite DB 구축
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 추가적인 메모리를 요하므로 꺼둔다.

db = SQLAlchemy(app)


###################### 모델 생성 ######################
# 모델은 DB에 테이블을 설정하는 것과 같다.
class Puppy(db.Model):
    # 클래스 이름을 기반으로 기본 테이블 이름이 제공되지만,
    # 다음과 같이 덮어쓸 수 있다.
    __tablename__ = 'puppies'


    # 참고로 SQLite에서 인덱스는 1부터 시작한다고 함.
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Puppy {self.name} is {self.age} year/s old"


# CREATES ALL THE TABLES MODEL --> DB TABLE
db.create_all()

puppy1 = Puppy('Sammy', 3)
puppy2 = Puppy('Frankie', 4)

db.session.add_all([puppy1, puppy2])
# 각각 추가하려는 경우에는 다음과 같이..
# db.session.add(puppy1)
# db.session.add(puppy2)

# 변경 사항을 데이터베이스에 저장
db.session.commit()

print("ids: ", puppy1.id, puppy2.id)


app_ctx.pop()