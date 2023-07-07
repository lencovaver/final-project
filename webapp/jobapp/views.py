from django.shortcuts import get_object_or_404, render
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostJobForm
from .models import PostJob


class HomepageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = PostJob.objects.all()
        return context


class AllJobsView(ListView):
    def get(self, request, *args, **kwargs):
        context = {
            "all_jobs": PostJob.objects.all()
        }

        return TemplateResponse(request, "all-jobs.html", context=context)


class JobDetailView(DetailView):
    model = PostJob
    context_object_name = 'job'
    template_name = "job-detail.html"

    def get_object(self):
        job_id = self.kwargs.get("job_id")
        return get_object_or_404(PostJob, id=job_id)


class JobCreateView(CreateView):
    model = PostJob
    form_class = PostJobForm
    template_name = 'create.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class JobUpdateView(UpdateView):
    model = PostJob
    form_class = PostJobForm
    template_name = 'update.html'
    success_url = '/'

    def get_success_url(self):
        return reverse_lazy('homepage')


class JobDeleteView(DeleteView):
    model = PostJob
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse_lazy('homepage')


class JobSearchView(ListView):
    model = PostJob
    template_name = "job-search.html"
    context_object_name = "jobs"

    def get_queryset(self):
        query = self.request.GET.get("position")
        print("Query:", query)
        if query:
            jobs = PostJob.objects.filter(positions__contains=query)
            print(jobs)  # Toto vypíše nalezené pracovní pozice do konzoly pro kontrolu
            return jobs
            # return PostJob.objects.filter(positions__contains=query)
        else:
            return PostJob.objects.all()
