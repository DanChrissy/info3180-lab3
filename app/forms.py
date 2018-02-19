from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class MyForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('E-mail', validators = [DataRequired(), Email()])
    subject = StringField('Subject', validators = [DataRequired()])
    message = TextAreaField('Message', validators = [DataRequired()])
   