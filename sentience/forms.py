from flask_wtf import FlaskForm
from wtforms import SubmitField,SelectField,StringField
from wtforms.validators import DataRequired
import csv


with open('/Users/OHHANJUN/Desktop/sentience/sentience/hs_code.csv', 'r',encoding='CP949') as f:
  reader = csv.reader(f)
  select_choices = [tuple(x) for x in reader]

class FindProduct(FlaskForm):
  product_type = SelectField('product_type', choices=select_choices, validators=[DataRequired()])
  country = SelectField('country',choices=[('US','국가선택'),('US','미국'),('TH','태국'),('ID','인도네시아'),('MY','말레이시아')])
  key_word = StringField('keyword',validators=[DataRequired()])
  submit = SubmitField("SEARCH")