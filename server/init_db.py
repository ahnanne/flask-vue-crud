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

    def __init__(self, name, age, breed) -> None:
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self) -> str:
        return f"[id: {self.id} / breed: {self.breed}] Puppy {self.name} is {self.age} year/s old"


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
