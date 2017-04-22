from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.utils.translation import gettext_lazy as _

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        labels = {
        	'display_name': _('Display Name / Company Name')
        }
        exclude = ['user', 'recommend', 'indifferent', 
        		   'donotrecommend',]
       	widgets = {'account_type': forms.HiddenInput()}


class Step2Form(forms.ModelForm):
    class Meta:
        model = Profile
        labels = {
        	'account_type': _('Company or Individual?'),
        	'display_name': _('Your name / Company Name')
        }
        help_texts = {
        	'account_type': _('Select whether you are a company or individual')
        }
        fields = ['account_type', 'display_name', 'image',]