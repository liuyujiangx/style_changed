from app import db


class Z_user(db.Model):
    __tablename__ = "z_user"
    id = db.Column(db.String(20), primary_key=True)
    username = db.Column(db.String(50))

    def __repr__(self):
        return "id %r" % self.id
class Imgs(db.Model):
    __tablename__ = "imgs"
    id = db.Column(db.Integer,primary_key=True)
    img_url = db.Column(db.String(255))
    img_name = db.Column(db.String(255))

if __name__ == '__main__':
    z_user = Z_user(
        id='5',
        username='liu'
    )
    db.session.add(z_user)
    db.session.commit()
