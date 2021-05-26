from django import forms
from django.contrib.auth.models import User
from learning1_app.models import UserInfoModel

class UserInfoForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username','email','password')
