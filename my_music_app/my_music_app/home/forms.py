from django import forms
from my_music_app.account.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']


class ProfileCreateForm(ProfileBaseForm):
    pass
