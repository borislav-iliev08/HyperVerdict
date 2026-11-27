import re

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
            'role': 'Are you Professional or Customer?',
        }
        error_messages={
            'email':{'required':"Don't forget this here!",'invalid':'Please provide valid email address!'},
            'first_name':{'required':"Don't forget this here!"},
            'last_name': {'required':"Don't forget this here!"},
            'role': {'required': "Don't forget this here!"},
            'password':{'required':"Don't forget this here!"},


        }
        labels={
            'role':'Account Type'
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


        user_candidate = UserModel(
            email=self.cleaned_data.get('email') or self.instance.email,
            first_name=self.cleaned_data.get('first_name') or self.instance.first_name,
            last_name=self.cleaned_data.get('last_name') or self.instance.last_name,
        )
        validate_password(password, user=user_candidate)
        return password

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =['user']
        widgets = {
            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter your age',
                'min': 18,
                'max': 110,
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number',
                'autocomplete': 'tel',
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'accept': 'image/*',
            }),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Tell us something about yourself',
                'rows': 5,
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Enter your city',
                'autocomplete': 'address-level2',
            }),
        }

        labels = {
            'age': 'Age',
            'phone_number': 'Phone Number',
            'profile_picture': 'Profile Picture',
            'bio': 'About Me',
            'city': 'City',
        }

        error_messages = {
            'age': {
                'invalid': 'Please enter a valid age.',
                'min_value': 'Age must be at least 18.',
                'max_value': 'You are not above 110 years old.',
            },
            'phone_number': {
                'invalid': 'Please enter a valid phone number.',
                'unique': 'This phone number is already registered.',
            },
            'profile_picture': {
                'invalid': 'Please upload a valid image.',
            },
            'bio': {
                'invalid': 'Please enter valid biography text.',
            },
            'city': {
                'invalid': 'Please enter a valid city.',
            },

        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")

        if not phone_number:
            return phone_number

        pattern = r"^\+?[\d\s()-]+$"
        if not re.match(pattern,phone_number):
            raise ValidationError(
                "Phone numbers can contain only: +, -, (, )."
            )

        return phone_number


    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if not bio is None:

            if len(bio)>300:
                raise ValidationError('Bio can\'t be over 300 symbols!')

        return bio

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if not city is None:

            if len(city)>20:
                raise ValidationError('City can\'t be over 20 symbols!')
        return city
