"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from jobapp.views import HomepageView, AllJobsView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView
from users.views import RegSuccessView, UserRegistrationView, AgentRegistrationView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomepageView.as_view(), name="homepage"),
    path("all-jobs/", AllJobsView.as_view(), name="all-jobs"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("business-registration/", AgentRegistrationView.as_view(), name="business-registration"),
    path("registration-success/", RegSuccessView.as_view(), name="registration-success"),
    path("job/<int:job_id>/", JobDetailView.as_view(), name='job-detail'),
    path("create/", JobCreateView.as_view(), name='create'),
    path("job/<int:pk>/update", JobUpdateView.as_view(), name='update'),
    path("job/<int:pk>/delete", JobDeleteView.as_view(), name='delete'),

]
