from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class CommentForm(FlaskForm):
    content = StringField('Comment')
    submit = SubmitField('Add Comment')