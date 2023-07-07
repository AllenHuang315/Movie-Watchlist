from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, URLField, PasswordField
from wtforms.validators import InputRequired, NumberRange, Email, Length, EqualTo


class MovieForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()]) 
    director = StringField("Director", validators=[InputRequired()])

    year = IntegerField(
        "Year",
        validators=[
            InputRequired(),
            NumberRange(min=1878, max=2024, message="Please enter a year format in 1878-2024.")
        ]
    )

    submit = SubmitField("Add Movie")

class StringListField(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []

class ExtendedMovieForm(MovieForm):
    cast = StringListField("Cast")
    series = StringListField("Series")
    tags = StringListField("Tags")
    description = TextAreaField("Description")
    video_link = URLField("Video link")

    submit = SubmitField("Submit")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()]) #"email"?
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            Length(min=6,
            max=20,
            message="Your password must be between 6 -20 chracters long.")
        ]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators= [
            InputRequired(),
            EqualTo(
                "password",
                message="Password did not match."
            )
        ]
    )
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()]) 
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")