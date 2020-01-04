from application import db


class Passwords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(200), unique=True, nullable=False)
    


    def __repf__(self):
        return "".join([
                "password: ", self.password
            ])

