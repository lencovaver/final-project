from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from users.forms import RegistrationForm


class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy("login")

    def post(self, request,  *args, **kwargs):
        registration_data = request.POST
        form = self.form_class(registration_data)
        if form.is_valid():
            form.save()
            return redirect('registration-success')
        else:
            return TemplateResponse(request, 'registration.html', context={'form': form})

    #def form_valid(self, form):
    #    valid = super().form_valid(form)
    #    username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
    #    user = User.objects.get(username=username)
    #    user.set_password(password)
    #    user.save()
    #    return valid


class RegSuccessView(View):

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'registration-success.html')

