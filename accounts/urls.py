from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetView, PasswordChangeDoneView, PasswordChangeView
from django.urls import path
from django.views import View

from accounts.views import RegistrationProfileView, LoginProfileView, DetailsProfileView, LogoutProfileView, \
    DeleteProfileView, UpdateProfileView

urlpatterns=[

    path('register/',RegistrationProfileView.as_view(),name='register'),
    path('login/',LoginProfileView.as_view(),name='login'),
    path('profile/<int:pk>/', DetailsProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/',UpdateProfileView.as_view(),name='edit'),
    path('logout/', LogoutProfileView.as_view(), name='logout'),
    path('profile/delete/<int:pk>/',DeleteProfileView.as_view(),name='delete'),
    path('password-change/', PasswordChangeView.as_view(template_name='accounts/password-change.html'),name='password-change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name='accounts/password-change-done.html'),name='password-change-done'),
    # password forgotten
    path('password-reset/', PasswordResetView.as_view(template_name='accounts/password-reset.html'), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name='accounts/password-reset-done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password-reset-confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='accounts/reset-done.html'), name='password_reset_complete'),
]
