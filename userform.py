from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
	first_name = StringField('First Name')
	age = IntegerField('Age')
	user_id = IntegerField('ID')
	submit = SubmitField('Enter')
	first_name_new = StringField('First Name')
	age_new = IntegerField('Age')
	mock_num = IntegerField('Number of rows')