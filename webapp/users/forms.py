from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import commit
from django import forms

from users.models import User, UserAgent, UserPerson, Company


class UserAgentRegistrationForm(UserCreationForm):
    agent_name = forms.CharField(max_length=50)
    agent_surname = forms.CharField(max_length=50)
    area_code = forms.ChoiceField(choices=[
        ("CZ", "+420"),
        ("SK", "+421"),
        ("CHE", "+41")
    ])
    phone = forms.IntegerField()
    company = forms.ModelChoiceField(queryset=Company.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'agent_name', 'agent_surname', 'area_code', 'phone',
                  'company']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_useragent = True
        if commit:
            user.save()
            UserAgent.objects.create(
                user=user,
                agent_name=self.cleaned_data['agent_name'],
                agent_surname=self.cleaned_data['agent_surname'],
                area_code=self.cleaned_data['area_code'],
                phone=self.cleaned_data['phone'],
                company=self.cleaned_data['company']
            )
        return user


class UserPersonRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    area_code = forms.ChoiceField(choices=[
        ("CZ", "+420"),
        ("SK", "+421"),
        ("CHE", "+41")
    ])
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'surname', 'area_code', 'phone']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_userperson = True
        if commit:
            user.save()
            UserPerson.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                surname=self.cleaned_data['surname'],
                area_code=self.cleaned_data['area_code'],
                phone=self.cleaned_data['phone']
            )
        return user
