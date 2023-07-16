from django.http import request, JsonResponse, Http404
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from .forms import PostJobForm
from .models import PostJob, Place, Language


from django.contrib import messages


class HomepageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        places = Place.objects.all()
        context["places"] = places

        context['jobs'] = PostJob.objects.all()
        return context


class AllJobsView(ListView):
    model = PostJob
    template_name = "all-jobs.html"
    context_object_name = "all_jobs"

    def get_queryset(self):
        return PostJob.objects.filter(status='active')


class JobDetailView(LoginRequiredMixin, DetailView):
    model = PostJob
    template_name = "job-detail.html"
    context_object_name = 'job'

    def get_object(self):
        job_id = self.kwargs.get("job_id")
        job = get_object_or_404(PostJob, id=job_id)
        if job.status != 'active':
            raise Http404
        return job


class JobCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = PostJob
    form_class = PostJobForm
    template_name = 'create.html'
    success_url = reverse_lazy('job-success')

    def test_func(self):
        return self.request.user.is_useragent or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission.")
        return redirect('homepage')

    def form_valid(self, form):
        form.instance.author = self.request.user
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        return redirect('job-success')


class JobUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = PostJob
    form_class = PostJobForm
    template_name = 'update.html'
    success_url = reverse_lazy('job-success')

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_superuser

    permission_required = 'jobapp.add_postjob'

    def handle_no_permission(self):
        messages.error(self.request, "No permission.")
        return redirect('homepage')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostJob
    template_name = 'delete.html'
    success_url = reverse_lazy('job-success')

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_superuser

    permission_required = 'jobapp.add_postjob'

    def handle_no_permission(self):
        messages.error(self.request, "No permission.")
        return redirect('homepage')

    def form_valid(self, form):
        response = super().delete(request)
        return response


class JobSuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'job-success.html')


class JobSearchView(ListView):
    model = PostJob
    template_name = "all-jobs.html"
    context_object_name = "jobs"

    def get_queryset(self):
        query = self.request.GET.get("title_contains")
        # print("Query:", query)
        if query:
            return PostJob.objects.filter(status='active', positions__name_position__icontains=query)
        else:
            return PostJob.objects.filter(status='active')


class PlaceSearchView(ListView):
    model = PostJob
    template_name = "all-jobs.html"
    context_object_name = "jobs"

    def get_queryset(self, *args, **kwargs):
        place_id = self.kwargs.get("place_id")

        jobs = PostJob.objects.filter(place__pk=place_id)
        return jobs


class LanguageSearchView(ListView):
    model = PostJob
    template_name = "all-jobs.html"
    context_object_name = "jobs"

    def get_queryset(self, *args, **kwargs):
        state_name = self.request.GET.get("state")

        jobs = PostJob.objects.filter(language__state=state_name)
        return jobs


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
    return JsonResponse({"message": "Success"})
