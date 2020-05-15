from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, HiddenField, RadioField, SelectField, SelectMultipleField
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.validators import DataRequired, Email, Length, InputRequired
from wtforms.widgets import CheckboxInput, ListWidget

class SignInForm(FlaskForm):
    email = StringField(label='Email address', id='email', validators=[
        Email(message='Email address has not been entered or is not the correct address.')
    ])
    password = PasswordField(label='Password', id='password', validators=[
        DataRequired(message='Please enter the password.')
    ])

class ContentForm(FlaskForm):
    content_id = HiddenField(label="Content id", id='content_id')
    content_title = StringField(label='Content title', id='content_title', validators=[
        DataRequired(message='Please enter a content title.')
    ])
    image = RadioField(label='Image', id='image', coerce=int,
        validate_choice=False
    )
    category = RadioField(label='Category', id='category', coerce=int,
        validate_choice=False
    )
    tags = SelectMultipleField(label='Tags', id='tags', coerce=int,
        widget=ListWidget(), option_widget=CheckboxInput(),
        validate_choice=False
    )
    status = RadioField(label='Status', id='status', coerce=int,
        choices=[(0, 'public'), (1, 'private')], default='1',
        validate_choice=False
    )
    description = TextAreaField(label='Description', id='description', validators=[
        DataRequired(message='Please enter a description.')
    ])
    content_text = CKEditorField(label='Content text', id='content_text', validators=[
        DataRequired(message='Please enter a content text.')
    ])
    commit = SubmitField(label='Commit', id='commit')
    delete = SubmitField(label='Delete', id='delete')

class ImageForm(FlaskForm):
    image_id = HiddenField(label="Image id", id='image_id')
    description = StringField(label='Description', id='description', validators=[
        DataRequired(message='Please enter a description.')
    ])
    image_file = FileField(label='Image File', id='image_file', validators=[
        FileRequired(),
        FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Images only!')
    ])
    commit = SubmitField(label='Commit', id='commit')