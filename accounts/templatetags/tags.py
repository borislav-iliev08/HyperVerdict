from django import template

from accounts.models import Profile

register = template.Library()

@register.simple_tag
def user_group_is_client(user)->bool:
    if user.groups.filter(name='Clients').exists():
        return True
    return False


@register.simple_tag
def user_registered_at(user:Profile,time_format='%Y-%m-%d %H:%M:%S'):
    return user.created_at.strftime(time_format)
