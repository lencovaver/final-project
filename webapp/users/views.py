from PIL import Image
import io
from django.core.files.base import ContentFile
from django.contrib import messages
from django.contrib.auth import logout
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
    # View for user registration.

    template_name = "registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("registration-success")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    # View for user login.

    template_name = "login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_useragent:
            return reverse("dashboard")
        else:
            return reverse("homepage")

    def form_invalid(self, form):
        return super().form_invalid(form)


class UserLogoutView(View):
    # View for user logout.

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("homepage")


class UserProfileView(DetailView):
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
    model = User
    form_class = EditProfileForm
    template_name = "edit-profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully!")
        return super().form_valid(form)

    def profile_pic_save(self, request, *args, **kwargs):
        user = self.get_object()
        form = EditProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            image_field = "company_logo" if user.is_useragent else "profile_pic"
            image = form.cleaned_data.get(image_field)

            if image:
                img = Image.open(image)
                output = io.BytesIO()

                resized_img = img.resize((300, 300))
                resized_img.save(
                    output, format="PNG", quality=85
                )  # Adjust quality according to your needs
                output.seek(0)  # move back to the beginning of the file stream

                django_file = ContentFile(output.read())
                django_file.name = (
                    image.name
                )  # make sure to keep the same name as the original file

                form.cleaned_data[image_field] = django_file

            form.save()
            return redirect("profile")
        else:
            return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        return self.profile_pic_save(request, *args, **kwargs)


class RegSuccessView(View):
    # View for showing registration success page.

    def get(self, request, *args, **kwargs):
        return render(request, "registration-success.html")
