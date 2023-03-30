from init_db import app, db, Puppy, Toy, Owner


app_ctx = app.app_context()
app_ctx.push()

# Create entries into the tables!

# Creating 2 puppies
puppy1 = Puppy('멍멍이', 3, '슈나우저')
puppy2 = Puppy('왈왈이', 5, '말티즈')

# Add puppies to db
db.session.add_all([puppy1, puppy2])
db.session.commit()

# Check!
print(Puppy.query.all())

puppy1 = Puppy.query.filter_by(name='멍멍이').all()[0]

# Create owner object
owner1 = Owner(name='강형욱', puppy_id=puppy1.id)

# 강아지에게 장난감을 몇 개 주자.
toy1 = Toy('Chew Toy', puppy1.id)
toy2 = Toy('Ball', puppy2.id)

db.session.add_all([owner1, toy1, toy2])
db.session.commit()

puppy1 = Puppy.query.filter_by(name='멍멍이').first()
print(puppy1)
puppy1.report_toys()


app_ctx.pop()
