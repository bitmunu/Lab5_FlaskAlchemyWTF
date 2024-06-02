from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('login', validators=[InputRequired(message="Заполните поле")])
    password = PasswordField('password', validators=[InputRequired(message="Заполните поле")])
    confirm_password = PasswordField('confirm password', validators=[
        InputRequired(message="Confirm."),
        EqualTo('password', message="Passwords don't match.")
    ])

    def validate_on_submit(self):
        return self.is_submitted() and self.validate()


class EditUserForm(FlaskForm):
    first_name = StringField('name', validators=[DataRequired(), Length(min=1, max=100)])
    last_name = StringField('family_name', validators=[DataRequired(), Length(min=1, max=100)])
    password = PasswordField('password', validators=[Length(min=6, max=128)])
    confirm_password = PasswordField('confirm password', validators=[EqualTo('password')])
    submit = SubmitField('Save')