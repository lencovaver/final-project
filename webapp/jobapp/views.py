from django.http import request, JsonResponse, Http404
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin,
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from .forms import PostJobForm
from .models import PostJob, Place, Language, PositionCategory, Position


from django.contrib import messages


class HomepageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        places = Place.objects.all()
        context["places"] = places

        context["jobs"] = PostJob.objects.all()
        return context


class AllJobsView(ListView):
    model = PostJob
    template_name = "all-jobs.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return PostJob.objects.filter(status="active")


class MyJobView(LoginRequiredMixin, ListView):
    model = PostJob
    template_name = "companydashboard.html"
    context_object_name = "dashboard"

    def get_queryset(self):
        print(f"Current user: {self.request.user}")
        jobs = PostJob.objects.filter(author=self.request.user)
        print(f"Jobs for user: {jobs}")
        return jobs


class JobDetailView(LoginRequiredMixin, DetailView):
    model = PostJob
    template_name = "job-detail.html"
    context_object_name = "job"

    def get_object(self):
        job_id = self.kwargs.get("job_id")
        job = get_object_or_404(PostJob, id=job_id)
        if job.status != "active":
            raise Http404
        return job


class JobCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = PostJob
    form_class = PostJobForm
    template_name = "create.html"

    def test_func(self):
        return self.request.user.is_useragent or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission.")
        return redirect("homepage")

    def form_valid(self, form):
        form.instance.author = self.request.user
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        return redirect("job-success")

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostJob
    form_class = PostJobForm
    template_name = "update.html"
    success_url = reverse_lazy("job-success")

    def test_func(self):
        job = self.get_object()
        return self.request.user == job.author or self.request.user.is_superuser

    permission_required = "jobapp.add_postjob"

    def handle_no_permission(self):
        messages.error(self.request, "No permission.")
        return redirect("homepage")

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostJob
    template_name = "delete.html"
    success_url = reverse_lazy("job-success")

    def test_func(self):
        return (
            self.request.user == self.get_object().author
            or self.request.user.is_superuser
        )

    permission_required = "jobapp.add_postjob"

    def handle_no_permission(self):
        messages.error(self.request, "No permission.")
        return redirect("homepage")

    def form_valid(self, form):
        response = super().delete(request)
        return response


class JobSuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "job-success.html")


class JobSearchView(ListView):
    model = PostJob
    template_name = "all-jobs.html"
    context_object_name = "jobs"

    def get_queryset(self):
        queryset = PostJob.objects.filter(status="active")
        query = self.request.GET.get("title_contains")
        if query:
            queryset = queryset.filter(position__name_position__icontains=query)

        place_id = self.request.GET.get("place_id")
        if place_id:
            queryset = queryset.filter(place__pk=place_id)

        state_name = self.request.GET.get("state")
        if state_name:
            queryset = queryset.filter(language__state=state_name)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Přidejme dostupné kantony a jazyky do kontextu
        context["places"] = Place.objects.all()
        context["languages"] = Language.objects.all()
        return context


class PlaceSearchView(ListView):
    model = PostJob
    template_name = "all-jobs.html"
    context_object_name = "jobs"

    def get_queryset(self):
        place_id = self.request.GET.get("place_id")
        if place_id:
            return PostJob.objects.filter(place__pk=place_id, status="active")
        else:
            return PostJob.objects.filter(status="active")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["postjobs"] = PostJob.objects.filter(status="active")
        return context


class LanguageSearchView(ListView):
    model = PostJob
    template_name = "all-jobs.html"
    context_object_name = "jobs"

    def get_queryset(self):
        state_name = self.request.GET.get("state")
        if state_name:
            return PostJob.objects.filter(language__state=state_name, status="active")
        else:
            return PostJob.objects.filter(status="active")


class JobArchiveView(ListView):
    model = PostJob
    template_name = "archiv.html"
    context_object_name = "archived_jobs"

    def get_queryset(self):
        return PostJob.objects.filter(status="archived")


@require_POST
def archive_job(request, pk):
    inzerat = get_object_or_404(PostJob, pk=pk)
    inzerat.archived = not inzerat.archived
    inzerat.save()
    inzerat_admin = PostJob.objects.get(pk=pk)
    inzerat_admin.status = "archived" if inzerat.archived else "active"
    inzerat_admin.save()
    return JsonResponse(
        {"message": "Inzerát je archivován.", "archived": inzerat.archived}
    )
