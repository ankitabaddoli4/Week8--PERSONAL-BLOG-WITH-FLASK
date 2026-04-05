from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    """Form for searching blog posts"""
    
    search = StringField(
        'Search',
        validators=[
            DataRequired(),
            Length(min=1, max=100)
        ]
    )
    
    submit = SubmitField('Search')