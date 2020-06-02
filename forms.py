from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """A form for adding new pets"""

    name = StringField("Pet's name", validators=[InputRequired()])
    species = SelectField("Pet's species", choices=[('dog', 'dog'), ('cat', 'cat'), ('porcy', 'porcupine')])
    photo_url = StringField("Link to the pet's photo", validators=[Optional(), URL()])
    age = IntegerField("Pet's age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """A form for adding new pets"""

    name = StringField("Pet's name", validators=[InputRequired()])
    species = SelectField("Pet's species", choices=[('dog', 'dog'), ('cat', 'cat'), ('porcy', 'porcupine')])
    photo_url = StringField("Link to the pet's photo", validators=[Optional(), URL()])
    age = IntegerField("Pet's age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])
    avaliable = BooleanField("Available:")