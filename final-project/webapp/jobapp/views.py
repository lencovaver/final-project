from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import PostJobForm
from .models import PostJob

from django.contrib import messages


class HomepageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = PostJob.objects.all()
        return context


class AllJobsView(ListView):
    model = PostJob
    template_name = "all-jobs.html"
    context_object_name = "all_jobs"


class JobDetailView(LoginRequiredMixin, DetailView):
    model = PostJob
    template_name = "job-detail.html"
    context_object_name = 'job'

    def get_object(self):
        job_id = self.kwargs.get("job_id")
        return get_object_or_404(PostJob, id=job_id)


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
        instance = form.save(commit=False)
        instance.save()

        form.save_m2m()

        return redirect('job-success')


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostJob
    form_class = PostJobForm
    template_name = 'update.html'
    success_url = reverse_lazy('job-success')

    def test_func(self):
        return self.request.user.is_useragent or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission.")
        return redirect('homepage')


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostJob
    template_name = 'delete.html'
    success_url = reverse_lazy('job-success')

    def test_func(self):
        return self.request.user.is_useragent or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission")
        return redirect('homepage')


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
            jobs = PostJob.objects.filter(positions__name_position__icontains=query)
            # print(jobs)  # Toto vypíše nalezené pracovní pozice do konzoly pro kontrolu
            return jobs
            # return PostJob.objects.filter(positions__contains=query)
        else:
            return PostJob.objects.all()
