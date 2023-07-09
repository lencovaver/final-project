from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.db.transaction import commit
from django import forms

from users.models import User
from jobapp.models import Language


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
            raise forms.ValidationError("This email is already in use.")
        return email


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    language = forms.ChoiceField(choices=Language.STATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    lang_level = forms.ModelChoiceField(queryset=Language.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    password = None

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            "address",
            "bio",
            "language",
            "lang_level",
            "area_code",
            "phone_number",
            "company"
        ]

