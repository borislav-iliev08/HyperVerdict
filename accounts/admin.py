from django.contrib import admin
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, AdminUserCreationForm
from django.utils.translation import gettext_lazy as _
# Register your models here.
UserModel = get_user_model()
@admin.register(UserModel)
class ProfileBaseUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("password",)}),
        (_("Personal info"), {"fields": ("email",'first_name','last_name','role')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('email','first_name','last_name','role',"usable_password", "password1", "password2"),
            },
        ),
    )
    form = UserChangeForm
    add_form = AdminUserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ("email",'first_name' ,'last_name', 'role', "is_staff")
    search_fields = ("email",'first_name')
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )