from app import app, db


app_ctx = app.app_context()
app_ctx.push()


###################### 모델 생성 ######################
# 모델은 DB에 테이블을 설정하는 것과 같다.

class Puppy(db.Model):
    # 클래스 이름을 기반으로 기본 테이블 이름이 제공되지만,
    # 다음과 같이 덮어쓸 수 있다.
    __tablename__ = 'puppies'


    # DB 인덱스는 1부터 시작
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    # 강아지 한 마리가 여러 장난감을 가질 수 있다고 가정한다. (일대다 -> uselist=True)
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')
    # lazy='dynamic' 옵션: item을 로드하는 대신, item을 로드하는 '쿼리'를 제공한다.

    # 모든 주인은 한 마리의 강아지만 가질 수 있다고 가정한다. (일대일 -> uselist=False)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name, age, breed) -> None:
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self) -> str:
        if self.owner:
            return f"강아지 이름은 {self.name}이고, 주인 이름은 {self.owner.name}이다."
        else:
            return f"강아지 이름은 {self.name}이고, 아직 주인은 없다!!"

    def report_toys(self):
        print("Here are my toys: ")

        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):

    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __int__(self, name, puppy_id):
        self.name = name;
        self.puppy_id = puppy_id


# CREATES ALL THE TABLES MODEL --> DB TABLE
db.create_all()

puppy1 = Puppy('Sammy', 3, '말티즈')
puppy2 = Puppy('Frankie', 4, '커여운 슈나우저')

db.session.add_all([puppy1, puppy2])
# 각각 추가하려는 경우에는 다음과 같이..
# db.session.add(puppy1)
# db.session.add(puppy2)

# 변경 사항을 데이터베이스에 저장
db.session.commit()

print("ids: ", puppy1.id, puppy2.id)


app_ctx.pop()
