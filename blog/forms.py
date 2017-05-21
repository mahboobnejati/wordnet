from wtforms.validators import ValidationError
from wtforms import Form, TextField, PasswordField, validators
from wtforms.fields.core import SelectField
from blog.models import *
from passlib.hash import bcrypt


def existUsername(form, field):
    if User(field.data).getUser():
        raise ValidationError('there is not karbar.')
            
class RegistrationForm(Form):
    firstname = TextField('name', [validators.Length(min=3, max=25, message='at least 3 character and maximum 25.')])
    lastname = TextField('family ', [validators.Length(min=3, max=25, message='at least 3 character and maximum 25.')])
    username = TextField('username', [existUsername, validators.Length(min=3, max=25, message='at least 3 character and maximum 25.')])
    email = TextField('email', [validators.Email(message='email is not correct.')])
    password = PasswordField('password', [
        validators.Required(message='set passwprd in nessecery.'),
        validators.EqualTo('confirm', message='repear is not correct.')
    ])
    confirm = PasswordField('repeat password')


class DResponseForm(Form):
    response = ''
    def __init__(self,stimulusId):
        response = TextField(stimulusId, [validators.Length(min=2, max=20,message='it should be at least 3 character')])
    
    
class MResponseForm(Form):
    def __init__(self,stimulusId):
        response = SelectField(stimulusId,choices=[])
    
    