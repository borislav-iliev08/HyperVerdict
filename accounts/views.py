import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

logger = logging.getLogger(__name__)
from accounts.forms import RegistrationProfileForm, EditProfileForm
from accounts.models import ProfileBaseUser, Profile


# Create your views here.
class RegistrationProfileView(CreateView):
    model = ProfileBaseUser
    form_class = RegistrationProfileForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        user = form.save(commit=False)
        raw_password = form.cleaned_data.get('password')
        if raw_password:
            user.set_password(raw_password)
        response = super().form_valid(form)
        try:
            send_mail(
                subject="Welcome to HyperVerdict – Your account is ready!!!",
                message=(
                    f"Hello, {self.object.first_name} {self.object.last_name}.\n"
                    f"Welcome to HyperVerdict!\nYour account has been successfully created. "
                    f"We're glad to have you with us.\n"
                    f"HyperVerdict connects you with legal and real estate professionals, "
                    f"making it easier to find expert assistance, schedule appointments, "
                    f"and manage your consultations in one place.\n\n"
                    f"What to do next:\n"
                    f"-Complete your profile.\n"
                    f"-Find an expert that matches your needs.\n"
                    f"-Schedule your first appointment.\n\n\n"
                    f"-Best regards,\nThe HyperVerdict Team!"
                ),
                from_email=None,
                recipient_list=[self.object.email],
                fail_silently=False,
            )
        except Exception as exc:
            logger.error(
                "Failed to send welcome email to %s: %s",
                self.object.email,
                exc,
            )

        return response





class LoginProfileView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')



class LogoutProfileView(LoginRequiredMixin,LogoutView):
    next_page = reverse_lazy('home')


class DetailsProfileView(LoginRequiredMixin, DetailView):
    model=Profile
    template_name = 'accounts/details.html'
    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(pk = self.request.user.pk).select_related('user')
        return query

class DeleteProfileView(LoginRequiredMixin,DeleteView):
    model= ProfileBaseUser
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(pk = self.request.user.pk)
        return query


class UpdateProfileView(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'accounts/edit.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(pk = self.request.user.pk).select_related('user')
        return query








