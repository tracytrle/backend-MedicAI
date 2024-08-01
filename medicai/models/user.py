from medicai.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    firstName = db.Column(db.String(150), nullable=True)
    middleName = db.Column(db.String(150), nullable=True)
    lastName = db.Column(db.String(150), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    dateOfBirth = db.Column(db.Date, nullable=True)
    city = db.Column(db.String(50), nullable=True)
    country = db.Column(db.String(50), nullable=True)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
