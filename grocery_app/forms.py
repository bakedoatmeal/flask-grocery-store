from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore,ItemCategory

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # : Add the following fields to the form class:
    # - title - StringField
    title = StringField('Grocery name', validators=[DataRequired()])
    # - address - StringField
    address = StringField('Address')
    # - submit button
    
def get_stores():
    return GroceryStore.query 

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # Add the following fields to the form class:
    # - name - StringField
    name = StringField('Name', validators=[DataRequired()])
    # - price - FloatField
    price = FloatField('Price')
    # - category - SelectField (specify the 'choices' param)
    category = SelectField('Category', choices=ItemCategory.choices())
    # - photo_url - StringField
    photo_url = StringField('Image')
    # - store - QuerySelectField (specify the `query_factory` param)
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query, allow_blank=False)
    # - submit button
