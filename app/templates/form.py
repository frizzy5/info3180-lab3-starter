from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import validators
from wtforms.widgets import TextArea



class ContactForm (FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    email = StringField('email', [validators.DataRequired(), validators.Email()])
    subject=StringField('subject',validators=[DataRequired()])
    text = StringField(u'Text', widget=TextArea())
    
    