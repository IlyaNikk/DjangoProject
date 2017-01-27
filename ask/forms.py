from django import forms
from django.contrib.auth.models import User
from ask.models import Profile
from django.forms import ModelForm
from ask.models import Question

class UserForm(forms.Form):
    username = forms.CharField(label = "Username", widget = forms.TextInput(attrs = {'class' : 'form-control'}))
    first_name = forms.CharField(label = "First name", widget = forms.TextInput(attrs = {'class' : 'form-control'}))
    last_name = forms.CharField(label = "Last Name", widget = forms.TextInput(attrs = {'class' : 'form-control'}))
    email = forms.CharField(label = "Email", widget = forms.EmailInput(attrs = {'class' : 'form-control'}))
    password = forms.CharField(label = "Password", widget = forms.PasswordInput(attrs = {'class' : 'form-control'}))
    repeat_password = forms.CharField(label = "Repeat Password", widget = forms.PasswordInput(attrs = {'class' : 'form-control'}))
    url_to_redirect = forms.CharField(label ='', widget = forms.TextInput(attrs = {'class' : 'form-control', 'type' : 'hidden'}) )

class SignUpForm(forms.Form):
    username = forms.CharField(label = "Username", widget = forms.TextInput(attrs = {'class' : 'form-control'}))
    password = forms.CharField(label = "Password", widget = forms.PasswordInput(attrs = {'class' : 'form-control'}))
    url_to_redirect = forms.CharField(label ='', widget = forms.TextInput(attrs = {'class' : 'form-control', 'type' : 'hidden'}) )

class QuestionForm(forms.Form):
    question_title = forms.CharField(label = "Title", widget = forms.TextInput(attrs = {'class' : 'form-control'}))
    question_text = forms.CharField(label = "Text", widget = forms.Textarea(attrs = {'class' : 'form-control'}))
    question_tag = forms.CharField(label = "Tag", widget = forms.TextInput(attrs = {'class' : 'form-control'}))

class AnswerForm(forms.Form):
    text = forms.CharField(label = "Your Answer", widget = forms.Textarea(attrs = {'class' : 'form-control', 'rows' : '3'}))
