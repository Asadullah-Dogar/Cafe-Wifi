# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, URLField, BooleanField
# from wtforms.validators import DataRequired, URL
# from datetime import datetime
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
# app = Flask(__name__)
# Bootstrap(app)
# app.secret_key = "supersecretkey"  # Secure this for production
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
# db = SQLAlchemy(app)
#
# app.secret_key = os.getenv("SECRET_KEY")
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
#
# class Config:
#     SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
#     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///cafes.db")
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
# # Apply configuration
# app.config.from_object(Config)
#
#
# # Database Model
# class Cafe(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250), unique=True, nullable=False)
#     location = db.Column(db.String(250), nullable=False)
#     img_url = db.Column(db.String(500), nullable=False)
#     map_url = db.Column(db.String(500), nullable=False)
#     has_wifi = db.Column(db.Boolean, nullable=False)
#     seats = db.Column(db.String(250), nullable=False)
#     has_sockets = db.Column(db.Boolean, nullable=False)
#     has_toilet = db.Column(db.Boolean, nullable=False)
#     can_take_calls = db.Column(db.Boolean, nullable=False)
#     coffee_price = db.Column(db.String(250), nullable=True)
#
# # Flask-WTForms
# class CafeForm(FlaskForm):
#     name = StringField('Cafe Name', validators=[DataRequired()])
#     map_url = URLField('Map URL', validators=[DataRequired(), URL()])
#     img_url = URLField('Image URL', validators=[DataRequired(), URL()])
#     location = StringField('Location', validators=[DataRequired()])
#     seats = StringField('Number of Seats (e.g., 30-40)', validators=[DataRequired()])
#     has_toilet = BooleanField('Does it have toilets?')
#     has_wifi = BooleanField('Does it have WiFi?')
#     has_sockets = BooleanField('Are there sockets?')
#     can_take_calls = BooleanField('Can you take calls?')
#     coffee_price = StringField('Average Coffee Price', validators=[DataRequired()])
#     submit = SubmitField('Submit')
#
# # Create Database
# with app.app_context():
#     db.create_all()
#
# @app.route("/")
# def home():
#     cafes = Cafe.query.all()
#     return render_template("index.html", cafes=cafes, now=datetime.now())
#
#
# @app.context_processor
# def inject_now():
#     return {'now': datetime.now()}
#
# @app.route("/add", methods=["GET", "POST"])
# def add():
#     form = CafeForm()
#     if form.validate_on_submit():
#         new_cafe = Cafe(
#             name=form.name.data,
#             location=form.location.data,
#             img_url=form.img_url.data,
#             map_url=form.map_url.data,
#             seats=form.seats.data,
#             has_wifi=form.has_wifi.data,
#             has_sockets=form.has_sockets.data,
#             has_toilet=form.has_toilet.data,
#             can_take_calls=form.can_take_calls.data,
#             coffee_price=form.coffee_price.data,
#         )
#         db.session.add(new_cafe)
#         db.session.commit()
#         flash("New cafe added successfully!")
#         return redirect(url_for("home"))
#     return render_template("add.html", form=form, is_edit=False)
#
# @app.route("/edit/<int:cafe_id>", methods=["GET", "POST"])
# def edit_cafe(cafe_id):
#     cafe = db.get_or_404(Cafe, cafe_id)
#     edit_form = CafeForm(
#         name=cafe.name,
#         map_url=cafe.map_url,
#         img_url=cafe.img_url,
#         location=cafe.location,
#         seats=cafe.seats,
#         has_toilet=bool(cafe.has_toilet),
#         has_wifi=bool(cafe.has_wifi),
#         has_sockets=bool(cafe.has_sockets),
#         can_take_calls=bool(cafe.can_take_calls),
#         coffee_price=cafe.coffee_price
#     )
#     if edit_form.validate_on_submit():
#         cafe.name = edit_form.name.data
#         cafe.map_url = edit_form.map_url.data
#         cafe.img_url = edit_form.img_url.data
#         cafe.location = edit_form.location.data
#         cafe.seats = edit_form.seats.data
#         cafe.has_toilet = bool(edit_form.has_toilet.data)
#         cafe.has_wifi = bool(edit_form.has_wifi.data)
#         cafe.has_sockets = bool(edit_form.has_sockets.data)
#         cafe.can_take_calls = bool(edit_form.can_take_calls.data)
#         cafe.coffee_price = edit_form.coffee_price.data
#         db.session.commit()
#         flash("Cafe updated successfully!")
#         return redirect(url_for("home"))
#     return render_template("add.html", form=edit_form, is_edit=True)
#
# @app.route("/delete/<int:cafe_id>", methods=["GET", "POST"])
# def delete_cafe(cafe_id):
#     cafe_to_delete = Cafe.query.get(cafe_id)
#     if request.method == "POST":
#         if cafe_to_delete:
#             db.session.delete(cafe_to_delete)
#             db.session.commit()
#             flash("Cafe deleted successfully!")
#         return redirect(url_for("home"))
#     return render_template("delete_cafe.html", cafe=cafe_to_delete)
#
# if __name__ == "__main__":
#     app.run(debug=True)
#








from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, BooleanField
from wtforms.validators import DataRequired, URL
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration Class
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")  # Fallback to a default key
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///cafes.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

Bootstrap(app)
db = SQLAlchemy(app)

# Database Model
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    location = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

# Flask-WTForms
class CafeForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired()])
    map_url = URLField('Map URL', validators=[DataRequired(), URL()])
    img_url = URLField('Image URL', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    seats = StringField('Number of Seats (e.g., 30-40)', validators=[DataRequired()])
    has_toilet = BooleanField('Does it have toilets?')
    has_wifi = BooleanField('Does it have WiFi?')
    has_sockets = BooleanField('Are there sockets?')
    can_take_calls = BooleanField('Can you take calls?')
    coffee_price = StringField('Average Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Create Database
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    cafes = Cafe.query.all()
    return render_template("index.html", cafes=cafes, now=datetime.now())

@app.context_processor
def inject_now():
    return {'now': datetime.now()}

@app.route("/add", methods=["GET", "POST"])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            location=form.location.data,
            img_url=form.img_url.data,
            map_url=form.map_url.data,
            seats=form.seats.data,
            has_wifi=form.has_wifi.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            can_take_calls=form.can_take_calls.data,
            coffee_price=form.coffee_price.data,
        )
        db.session.add(new_cafe)
        db.session.commit()
        flash("New cafe added successfully!")
        return redirect(url_for("home"))
    return render_template("add.html", form=form, is_edit=False)

@app.route("/edit/<int:cafe_id>", methods=["GET", "POST"])
def edit_cafe(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    edit_form = CafeForm(
        name=cafe.name,
        map_url=cafe.map_url,
        img_url=cafe.img_url,
        location=cafe.location,
        seats=cafe.seats,
        has_toilet=bool(cafe.has_toilet),
        has_wifi=bool(cafe.has_wifi),
        has_sockets=bool(cafe.has_sockets),
        can_take_calls=bool(cafe.can_take_calls),
        coffee_price=cafe.coffee_price
    )
    if edit_form.validate_on_submit():
        cafe.name = edit_form.name.data
        cafe.map_url = edit_form.map_url.data
        cafe.img_url = edit_form.img_url.data
        cafe.location = edit_form.location.data
        cafe.seats = edit_form.seats.data
        cafe.has_toilet = bool(edit_form.has_toilet.data)
        cafe.has_wifi = bool(edit_form.has_wifi.data)
        cafe.has_sockets = bool(edit_form.has_sockets.data)
        cafe.can_take_calls = bool(edit_form.can_take_calls.data)
        cafe.coffee_price = edit_form.coffee_price.data
        db.session.commit()
        flash("Cafe updated successfully!")
        return redirect(url_for("home"))
    return render_template("add.html", form=edit_form, is_edit=True)

@app.route("/delete/<int:cafe_id>", methods=["GET", "POST"])
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    if request.method == "POST":
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            flash("Cafe deleted successfully!")
        return redirect(url_for("home"))
    return render_template("delete_cafe.html", cafe=cafe_to_delete)

if __name__ == "__main__":
    app.run(debug=True)
