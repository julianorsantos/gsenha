# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from flask.ext.appbuilder.forms import DynamicForm
from wtforms import StringField, SubmitField, PasswordField, RadioField, HiddenField, SelectMultipleField, SelectField, IntegerField, TextAreaField
from wtforms.validators import Required, DataRequired, Length, EqualTo

class LoginForm(Form):
    user = StringField('Username', validators=[Required(), Length(1,256)])
    password = PasswordField('Password', validators=[Required(),Length(1,256)])   
    submit = SubmitField('Submit')

class AddPasswordPersonalForm(Form): 
	name = StringField('Name',validators=[Required(),Length(1,256)])
	passwd = PasswordField('Password',validators=[Required(),Length(1,256),EqualTo('passwd2', message=u'Passwords are not the same.')])
	passwd2 = PasswordField('Confirm Password',validators=[Required(),Length(1,256)])
	folder = SelectField('Folder',validators=[Required()],coerce=str)
	login = StringField('Login',validators=[Required(),Length(1,256)])
	url = StringField('Url',validators=[Length(0,256)])
	description = TextAreaField(u'Description',validators=[Required(),Length(1,256)])
	submit = SubmitField('Submit')

class AddPasswordGroupForm(Form): 
	name = StringField('Name',validators=[Required(),Length(1,256)])
	passwd = PasswordField('Password',validators=[Required(),Length(1,256),EqualTo('passwd2', message=u'Passwords are not the same.')])
	passwd2 = PasswordField('Confirm Password',validators=[Required(),Length(1,256)])
	folder = SelectField('Folder',validators=[Required()],coerce=str)
	group = SelectField('Group',coerce=str)
	login = StringField('Login',validators=[Required(),Length(1,256)])
	url = StringField('Url',validators=[Length(0,256)])
	description = TextAreaField(u'Description',validators=[Required(),Length(1,256)])
	submit = SubmitField('Submit')

class AddPasswordExtUserForm(Form):
	name = StringField('Name',validators=[Required(),Length(1,256)])
	passwd = PasswordField('Password',validators=[Required(),Length(1,256),EqualTo('passwd2', message=u'Passwords are not the same.')])
	passwd2 = PasswordField('Confirm Password',validators=[Required(),Length(1,256)])
	username = StringField('Username',validators=[Required(),Length(1,256)])
	login = StringField('Login',validators=[Required(),Length(1,256)])
	url = StringField('Url',validators=[Length(0,256)])
	description = TextAreaField(u'Description',validators=[Required(),Length(1,256)])
	submit = SubmitField('Submit')

class AddPasswordExtGroupForm(Form):
	name = StringField('Name',validators=[Required(),Length(1,256)])
	passwd = PasswordField('Password',validators=[Required(),Length(1,256),EqualTo('passwd2', message=u'Passwords are not the same.')])
	passwd2 = PasswordField('Confirm Password',validators=[Required(),Length(1,256)])
	group = SelectField('Group',coerce=str)	
	login = StringField('Login',validators=[Required(),Length(1,256)])
	url = StringField('Url',validators=[Length(0,256)])
	description = TextAreaField(u'Description',validators=[Required(),Length(1,256)])
	submit = SubmitField('Submit')
    
class AddUserForm(Form):
	user = StringField('Username',validators=[Required(),Length(1,256)])
	password = PasswordField('Password',validators=[Required(),Length(1,256)])
	pk = TextAreaField('Public Key',validators=[Required(),Length(1,1500)])
	submit = SubmitField('Submit')

class AddFolderForm(Form):
	path = SelectField('Path',coerce=str,validators=[Required()])
	name = StringField('Name',validators=[Required(),Length(1,256)])
	submit = SubmitField('Submit')

class DeleteFolderForm(Form):
	folder = SelectField('Folder',coerce=str,validators=[Required()])
	submit = SubmitField('Submit')	

class UnlockForm(Form):
	usertounlock = StringField(u'User to unlock',validators=[Required(),Length(1,256)])
	group = SelectField('Group',validators=[Required()],coerce=str)
	submit = SubmitField('Submit')

class UpdatePasswdForm(Form):
	id_passwd = HiddenField('ID',validators=[Required()])
	passwd = PasswordField('Password',validators=[Length(0,256),EqualTo('passwd2', message=u'Passwords are not tha same')])
	passwd2 = PasswordField('Confirm Password',validators=[Length(0,256)])
	url = StringField('Url',validators=[Length(0,256)])
	login = StringField('Login',validators=[Length(0,256)])
	name = StringField('Name',validators=[Length(0,256)])
	description = StringField(u'Description',validators=[Length(0,256)])
	submit = SubmitField('Submit')

class UpdatePubKeyForm(Form):
	pubkey = TextAreaField('New Public Key',validators=[Required(),Length(1,1500)])
	privkey = TextAreaField('Current Private Key',validators=[Required(),Length(1,4000)])
	submit = SubmitField('Submit')

class DeletePasswordForm(Form):
	id_passwd = IntegerField('Password ID',validators=[Required()])
	submit = SubmitField('Submit')