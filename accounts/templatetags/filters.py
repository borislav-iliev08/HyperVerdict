from django import template

from accounts.models import Profile

register = template.Library()

@register.filter
def form_user_name(value: Profile)->str:
    return f'{value.first_name} {value.last_name}'


@register.filter
def check_if_profile_is_completed(value)-> bool:
    required_fields_for_completion = [value.phone_number,value.bio,value.city,value.profile_picture]
    for i in required_fields_for_completion:
        if i is None or i =='':
            return False
    return True

