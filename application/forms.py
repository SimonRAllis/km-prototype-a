from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired

class searchForm(Form):
    searchArea = SelectField('Search Area', choices=[('all', 'All'), ('reg', 'Registration'), ('info', 'Information Services'), ('cust', 'Customer Handling')])
    searchString = StringField("Search String")
    submit = SubmitField("Search")

class uploadContentForm(Form):
    uploadfiles = StringField('uploadfiles', validators=[DataRequired()])

class uploadResultsForm(Form):
    submit = SubmitField("OK")
