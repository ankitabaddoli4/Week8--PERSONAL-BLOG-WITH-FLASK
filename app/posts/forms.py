from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class PostForm(FlaskForm):
    title = StringField('Title')
    submit = SubmitField('Post')