from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """A class for pets in the shelter"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.String)
    age = db.Column(db.Integer)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean, default=True)

    def edit_pet(self, name, species, photo_url, age, notes, available):
        self.name = name
        self.species = species
        self.photo_url = photo_url
        self.age = age
        self.notes = notes
        self.available = available

        db.session.commit()


