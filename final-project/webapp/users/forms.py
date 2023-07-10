from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms

from users.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "is_useragent")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    company_name = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            "address",
            "bio",
            "area_code",
            "phone_number",
            "company_name"
        ]
        exclude = ['password', "company"]

