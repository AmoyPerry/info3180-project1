from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class PropForm(FlaskForm):

    title = StringField('Property Title', validators=[InputRequired()])
    descr = TextAreaField('Description', validators=[InputRequired()])
    numRooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    numBaths = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    propType = SelectField('Property Type', choices=[('Housing', 'Housing'), ('Apartment', 'Apartment')], validators=[InputRequired()]) 
    location = TextAreaField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[ FileRequired(),FileAllowed(['jpg', 'jpeg', 'png'])])
    