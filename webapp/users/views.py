from PIL import Image
import io
from django.core.files.base import ContentFile
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from users.forms import RegistrationForm, EditProfileForm
from users.models import User
from django.shortcuts import redirect


class RegistrationView(CreateView):
    """
    View for user registration.
    """

    template_name = "registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("registration-success")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class UserLoginView(LoginView):
    """
    View for user login.
    """

    template_name = "login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        print(f"Trying to log in user: {self.request.POST.get('username')}")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(f"Login failed for user: {self.request.POST.get('username')}")
        return super().form_invalid(form)

    def get_success_url(self):
        if self.request.user.is_useragent:
            return reverse("dashboard")
        else:
            return reverse("homepage")


class UserLogoutView(View):
    """View for user logout."""

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("homepage")


class UserProfileView(DetailView):
    """View for user profile."""

    model = User
    form_class = EditProfileForm
    template_name = "profile.html"

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()

        if user.is_useragent:
            context["company"] = user.company
            pic = user.company_logo
        else:
            pic = user.profile_pic
            context["profile_pic"] = pic
        return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    """View for editing user profile."""

    model = User
    form_class = EditProfileForm
    template_name = "edit-profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        messages.info(self.request, "POST request received")
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        user = self.request.user
        image_field = "company_logo" if user.is_useragent else "profile_pic"
        image = form.cleaned_data.get(image_field)

        if image:
            img = Image.open(image)
            output = io.BytesIO()

            resized_img = img.resize((300, 300))
            resized_img.save(output, format="PNG", quality=85)
            output.seek(0)

            django_file = ContentFile(output.read())
            django_file.name = image.name

            setattr(user, image_field, django_file)

        messages.success(self.request, "Profile updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, f"Form validation failed: {form.errors}")
        return super().form_invalid(form)


class RegSuccessView(View):
    """View for registration success."""

    def get(self, request, *args, **kwargs):
        return render(request, "registration-success.html")
