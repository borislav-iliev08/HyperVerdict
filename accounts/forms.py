from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from accounts.models import ProfileBaseUser, Profile

UserModel = get_user_model()
class RegistrationProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileBaseUser
        fields =['email','first_name','last_name','role','password']

        widgets = {
            'email':forms.EmailInput(attrs={'placeholder':'Enter your email here!'}),
            'first_name':forms.TextInput(attrs={'placeholder': 'Enter your first name here!'}),
            'last_name':forms.TextInput(attrs={'placeholder': 'Enter your last name here!'}),
            'role':forms.RadioSelect(),
            'password':forms.PasswordInput(attrs={'placeholder': 'Enter your password here!'}),
        }
        help_texts = {
            'role': 'Are you Professional or Client?',
        }
        error_messages={
            'email':{'required':"Don't forget this here!"},
            'first_name':{'required':"Don't forget this here!"},
            'last_name': {'required':"Don't forget this here!"},
            'password':{'required':"Don't forget this here!"},


        }

    def _clean_name(self, value, field_label):
        cleaned = (value or '').strip()
        if not cleaned:
            raise ValidationError(f'{field_label} cannot be blank or spaces only.')
        if len(cleaned) < 2:
            raise ValidationError(f'{field_label} must be at least 2 characters long.')
        return cleaned

    def clean_first_name(self):
        return self._clean_name(self.cleaned_data.get('first_name'), 'First name')

    def clean_last_name(self):
        return self._clean_name(self.cleaned_data.get('last_name'), 'Last name')

    def clean_email(self):
        email = (self.cleaned_data.get('email') or '').strip().lower()
        if not email:
            raise ValidationError("Don't forget this here!")

        if UserModel.objects.filter(email__iexact=email).exists():
            raise ValidationError('An account with this email already exists.')

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError("Don't forget this here!")

        user_candidate = UserModel(
            email=self.cleaned_data.get('email') or self.instance.email,
            first_name=self.cleaned_data.get('first_name') or self.instance.first_name,
            last_name=self.cleaned_data.get('last_name') or self.instance.last_name,
        )
        validate_password(password, user=user_candidate)
        return password

    def clean_role(self):
        role = self.cleaned_data.get('role')
        if not role:
            raise ValidationError('Please select a role.')
        return role

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

