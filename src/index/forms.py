from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class DataForm(FlaskForm):
    usernames = StringField(validators=[InputRequired()])
    emails = StringField(validators=[InputRequired()])
    name = StringField(validators=[InputRequired()])
    organisations = StringField()
    domains = StringField()

    submit = SubmitField()
