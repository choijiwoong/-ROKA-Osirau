import datetime

from django import forms
from .models import Req_gui, Req_use, User_info, Guide_info

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class Req_guiForm(forms.ModelForm):
	class Meta:
		model=Req_gui
		fields=('name', 'location', 'latitude', 'longitude', 'introduce','email')

class Req_useForm(forms.ModelForm):
	class Meta:
		model=Req_use
		fields=('name', 'location', 'latitude', 'longitude', 'introduce','email')

class Regis_guideForm(forms.ModelForm):
	class Meta:
		model=Guide_info
		fields=('name', 'password', 'email','identify_num')

class Regis_userForm(forms.ModelForm):
	class Meta:
		model=User_info
		fields=('name', 'password', 'email', 'dis_identify_num')