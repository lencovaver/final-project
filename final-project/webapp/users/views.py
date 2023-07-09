from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from users.forms import RegistrationForm, EditProfileForm

from users.models import User


class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration-success')
        else:
            return render(request, self.template_name, {'form': form})


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('homepage')


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
        messages.success(self.request, 'Your profile was successfully updated!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the error below.')
        return super().form_invalid(form)


class RegSuccessView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'registration-success.html')
