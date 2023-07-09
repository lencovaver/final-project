from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.db.transaction import commit
from django import forms

from users.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


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


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
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
            'email',
            "area_code",
            "phone_number",
            "company"
        ]


#class RegistrationForm2(UserCreationForm):
#    agent_name = forms.CharField(max_length=50)
#    agent_surname = forms.CharField(max_length=50)
#    area_code = forms.ChoiceField(choices=[
#        ("CZ", "+420"),
#        ("SK", "+421"),
#        ("CHE", "+41")
#    ])
#    phone = forms.IntegerField()
#    company = forms.ModelChoiceField(queryset=Company.objects.all())
#
#    class Meta:
#        model = User
#        fields = ['username', 'email', 'password1', 'password2', 'agent_name', 'agent_surname', 'area_code', 'phone',
#                  'company']
#
#    def save(self, commit=True):
#        user = super().save(commit=False)
#        user.is_useragent = True
#        if commit:
#            user.save()
#            UserAgent.objects.create(
#                user=user,
#                agent_name=self.cleaned_data['agent_name'],
#                agent_surname=self.cleaned_data['agent_surname'],
#                area_code=self.cleaned_data['area_code'],
#                phone=self.cleaned_data['phone'],
#                company=self.cleaned_data['company']
#            )
#        return user


#class UserPersonRegistrationForm(UserCreationForm):
#    first_name = forms.CharField(max_length=50)
#    surname = forms.CharField(max_length=50)
#    area_code = forms.ChoiceField(choices=[
#        ("CZ", "+420"),
#        ("SK", "+421"),
#        ("CHE", "+41")
#    ])
#    phone = forms.IntegerField()
#
#    class Meta:
#        model = User
#        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'surname', 'area_code', 'phone']
#
#    def save(self, commit=True):
#        user = super().save(commit=False)
#        user.is_userperson = True
#        if commit:
#            user.save()
#            UserPerson.objects.create(
#                user=user,
#                first_name=self.cleaned_data['first_name'],
#                surname=self.cleaned_data['surname'],
#                area_code=self.cleaned_data['area_code'],
#                phone=self.cleaned_data['phone']
#            )
#        return user
