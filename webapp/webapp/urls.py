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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from jobapp.views import (
    HomepageView,
    AllJobsView,
    JobDetailView,
    JobCreateView,
    JobUpdateView,
    JobDeleteView,
    JobSearchView,
    JobSuccessView,
    PlaceSearchView,
    LanguageSearchView,
    JobArchiveView,
    MyJobView,
)
from jobapp.views import archive_job
from users.views import (
    RegSuccessView,
    RegistrationView,
    UserLoginView,
    UserLogoutView,
    EditProfileView,
    UserProfileView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomepageView.as_view(), name="homepage"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path(
        "registration-success/", RegSuccessView.as_view(), name="registration-success"
    ),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("profile/edit", EditProfileView.as_view(), name="edit-profile"),
    path("all-jobs/", AllJobsView.as_view(), name="all-jobs"),
    path("dashboard/", MyJobView.as_view(), name="dashboard"),
    path("job/<int:job_id>/", JobDetailView.as_view(), name="job-detail"),
    path("create/", JobCreateView.as_view(), name="create"),
    path("job-success/", JobSuccessView.as_view(), name="job-success"),
    path("job/<int:pk>/update", JobUpdateView.as_view(), name="update"),
    path("job/<int:pk>/delete", JobDeleteView.as_view(), name="delete"),
    path("job-search/", JobSearchView.as_view(), name="job-search"),
    path("job/place/<int:place_id>/", PlaceSearchView.as_view(), name="place-search"),
    path("state-search/", LanguageSearchView.as_view(), name="state-search"),
    path("archiv/", JobArchiveView.as_view(), name="job-archive"),
    path("archivovat/<int:pk>/", archive_job, name="archive-job"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
