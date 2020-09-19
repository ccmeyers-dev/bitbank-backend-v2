from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Account


def check_length(value):
    if len(value) < 8:
        raise forms.ValidationError(
            "Password must be at least 8 characters to meet our security standards")


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(), validators=[check_length, ])

    password2 = forms.CharField(
        widget=forms.PasswordInput(), validators=[check_length, ])

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'password', 'password2')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
            self.add_error('password2', "Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
