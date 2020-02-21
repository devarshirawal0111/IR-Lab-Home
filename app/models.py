from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    scholarLink = db.Column(db.String(120))
    linkedInLink = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Author = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)