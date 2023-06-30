from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import TemplateView

from .models import PostJob


class HomepageView(TemplateView):
    template_name = "homepage.html"


class AllJobsView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "all_jobs": PostJob.objects.all()
        }

        return TemplateResponse(request, "all-jobs.html", context=context)
