from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class CountryForm(Form):
    name = StringField('Where are you going?', validators=[Required()])
    submit = SubmitField('Submit')


