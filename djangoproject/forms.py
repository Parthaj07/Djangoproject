from django import forms
from django.core.exceptions import ValidationError
from patient.models import Patient
from doctor.models import Doctor

class PatientSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'password', 'confirm_password', 'address', 'city', 'state', 'pincode']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return cleaned_data

class DoctorSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'password', 'confirm_password', 'address', 'city', 'state', 'pincode']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return cleaned_data


