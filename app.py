from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = 'haveyourcatspayedornuetered'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('agency-home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Add pet form, handle adding a pet"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('add-pet-form.html', form=form)


@app.route('/display/<pet_id>')
def display_pet_info(pet_id):

    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet-info.html', pet=pet)

@app.route('/edit/<pet_id>', methods=["GET", "POST"])
def edit_pet_info(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        db.session.commit()
        flash(f"{pet.name} has been updated")
        return redirect(f"/display/{pet.id}")

    else: return render_template('edit-pet-form.html', form=form, pet=pet)