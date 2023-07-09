from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from users.forms import RegistrationForm, EditProfileForm, UserLoginForm
from users.models import User


class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy("registration-success")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('homepage')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('homepage')


class UserProfileView(DetailView):
    model = User
    form_class = EditProfileForm
    template_name = "profile.html"

    def get_object(self):
        return self.request.user


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = "edit-profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class RegSuccessView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'registration-success.html')
