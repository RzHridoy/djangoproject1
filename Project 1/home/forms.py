from django.contrib.auth.models import User

from django import forms
from home import models


class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = '__all__'


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ('facebook_id','profile_picture')
