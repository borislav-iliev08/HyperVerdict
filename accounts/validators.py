

from django.core.exceptions import ValidationError
from django.utils.translation import gettext


class MinimumLengthValidator:
    def __init__(self,min_length =10):
        self.min_length = min_length


    def validate(self,password,user = None):
        if len(password) < self.min_length:
            raise ValidationError(gettext('Your password must be at least 8 characters long!'),code='password_too_short',params={'min_length': self.min_length})

    def get_help_text(self):
        return gettext(
            "Your password must contain at least %(min_length)d characters."
            % {"min_length": self.min_length}
        )



