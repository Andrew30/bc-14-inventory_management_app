from flask_wtf import Form
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired


class AddAssets(Form):
    name = StringField('Asset Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    serial = StringField('Serial Number', validators=[DataRequired()])
    date = DateField('DatePicker', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AssignAsset(Form):
    name = StringField('Asset Name', validators=[DataRequired()])
    person = StringField('Assigned To', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    transaction = StringField('Transaction ID', validators=[DataRequired()])
    serial = StringField('Serial Number', validators=[DataRequired()])
    da = DateField('DatePicker', validators=[DataRequired()])
    dt = DateField('DatePicker', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ClaimAssets(Form):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    person = StringField('Assigned To', validators=[DataRequired()])
    serial = StringField('Serial Number', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LostItems(Form):
    name = StringField('Asset Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    serial = StringField('Serial Number', validators=[DataRequired()])
    da = DateField('DatePicker', validators=[DataRequired()])
    dt = DateField('DatePicker', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Notices(Form):
    name = StringField('Asset Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AssignedAssets(Form):
    name = StringField('Asset Name', validators=[DataRequired()])
    person = StringField('Assigned To', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    transaction = StringField('Transaction ID', validators=[DataRequired()])
    serial = StringField('Serial Number', validators=[DataRequired()])
    da = DateField('DatePicker', validators=[DataRequired()])
    dt = DateField('DatePicker', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ListAssets(Form):
    name = StringField('Asset Name', validators=[DataRequired()])
    person = StringField('Assigned To', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    transaction = StringField('Transaction ID', validators=[DataRequired()])
    serial = StringField('Serial Number', validators=[DataRequired()])
    da = DateField('DatePicker', validators=[DataRequired()])
    dt = DateField('DatePicker', validators=[DataRequired()])
    submit = SubmitField('Submit')