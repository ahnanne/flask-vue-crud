from app import app
from init_db import db, Puppy

app_ctx = app.app_context()
app_ctx.push()


## CREATE ##
my_puppy = Puppy('Rufus', 5, '시츄')
db.session.add(my_puppy)
db.session.commit()


## READ ##
all_puppies = Puppy.query.all()  # 테이블에 있는 모든 강아지 객체들
print(all_puppies)

# FILTERS
puppy2 = Puppy.query.filter_by(name='Frankie').all()

# SELECT BY ID
puppy1 = Puppy.query.get(1)
if puppy1 is None:
    puppy1 = puppy2[0]
else:
    print(puppy1.name)


## UPDATE ##
puppy1.age = 100
db.session.add(puppy1)
db.session.commit()


## DELETE ##
puppy3 = Puppy.query.get(2)
print(puppy3)  # 존재하지 않을 경우 None
if puppy3 is not None:
    db.session.delete(puppy3)
    db.session.commit()
else:
    print('삭제할 대상이 존재하지 않습니다.')

all_puppies = Puppy.query.all()
print(all_puppies)


app_ctx.pop()
