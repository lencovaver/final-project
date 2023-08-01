from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from django.core.exceptions import ValidationError

from users.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "is_useragent")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

    def clean_email(self):
        """
        Checks if email is already in use.
        #FIX ERROR MESSAGE!
        """

        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = [
            "profile_pic",
            "company_logo",
            "first_name",
            "last_name",
            "address",
            "bio",
            "phone_number",
            "company",
        ]
        exclude = ["password"]

    def clean_profile_pic(self):
        # Checks if profile picture is too large.

        image = self.cleaned_data.get("profile_pic", False)
        if image and image.size > 1 * 1024 * 1024:
            raise ValidationError("Image file too large - must be no more than 1MB")
        return image

    def clean_company_logo(self):
        # Checks if company logo is too large.

        image = self.cleaned_data.get("company_logo", False)
        if image and image.size > 1 * 1024 * 1024:
            raise ValidationError("Image file too large - must be no more than 1MB")
        return image
