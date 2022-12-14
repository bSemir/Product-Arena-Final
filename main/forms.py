from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from main.models import User


class RegisterForm(FlaskForm):
    #when I name my func like this, Flask will recognize it
    def validate_username(self, existing_username):
        user = User.query.filter_by(username=existing_username.data).first()
        if user:
            raise ValidationError('Wrong credentials!')

    def validate_email_address(self, existing_email_addres):
        email_address = User.query.filter_by(email_address=existing_email_addres.data).first()
        if email_address:
            raise ValidationError('Wrong credentials! Please try again.')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = StringField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')