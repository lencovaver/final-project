from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from webapp.users.forms import RegistrationForm


# class LoginView(FormMixin, TemplateView):
#     template_name = 'login.html'
#     form_class = AuthenticationForm
#
#     def post(self, request, *args, **kwargs):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('homepage')
#
#         return redirect('login')
#
#
# class LogoutView(View):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('homepage')
#
#
# class RegistrationView(FormMixin, TemplateView):
#     template_name = "registration.html"
#     form_class = RegistrationForm
#
#     def post(self, request,  *args, **kwargs):
#         registration_data = request.POST
#         form = self.form_class(registration_data)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         else:
#             return TemplateResponse(request, 'registration.html', context={'form': form})
