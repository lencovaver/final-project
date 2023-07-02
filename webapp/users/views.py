from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic.edit import CreateView

from users.forms import UserAgentRegistrationForm, UserPersonRegistrationForm


class UserRegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = UserPersonRegistrationForm

    def post(self, request, *args, **kwargs):
        registration_data = request.POST
        form = self.form_class(registration_data)
        if form.is_valid():
            form.save()
            return redirect('registration-success')
        else:
            print(form.errors)
            return TemplateResponse(request, 'registration.html', context={'form': form})


class AgentRegistrationView(CreateView):
    template_name = 'business-registration.html'
    form_class = UserAgentRegistrationForm

    def post(self, request, *args, **kwargs):
        registration_data = request.POST
        form = self.form_class(registration_data)
        if form.is_valid():
            form.save()
            return redirect('registration-success')
        else:
            print(form.errors)
            return TemplateResponse(request, 'business-registration.html', context={'form': form})


class RegSuccessView(View):

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'registration-success.html')
