from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError

class DataForm(FlaskForm):
    usernames = StringField(validators=[InputRequired()])
    emails = StringField(validators=[InputRequired()])
    name = StringField(validators=[InputRequired()])
    organisations = StringField()
    domains = StringField()

    submit = SubmitField()
