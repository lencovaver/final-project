from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, Http404
from django.views.generic import ListView, DetailView, FormView, DeleteView
from jobapp.models import PostJob
from message.forms import MessageForm
from message.models import Message
from users.models import User


class InboxView(LoginRequiredMixin, ListView):
    """Display all messages in the user's inbox."""

    model = Message
    template_name = "inbox.html"
    context_object_name = "inbox"

    def get_queryset(self):
        return Message.objects.filter(
            Q(recipient=self.request.user) | Q(sender=self.request.user),
            is_archived=False,
        ).order_by("-timestamp")


class MessageView(LoginRequiredMixin, DetailView):
    """Display a single message."""

    model = Message
    template_name = "message.html"
    context_object_name = "message"

    def get_object(self, queryset=None):
        message_id = self.kwargs.get("pk")
        message = get_object_or_404(Message, id=message_id)

        if message.recipient != self.request.user:
            raise Http404("Ups. Chyba.")

        if not message.is_read:
            message.is_read = True
            message.save()

        return message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = self.object.job
        context.update(
            {
                "job": job,
                "position_name": job.position.name_position if job else None,
                "place": job.place if job else None,
            }
        )
        return context


class ComposeMessageView(LoginRequiredMixin, FormView):
    """Display a form for composing a new message."""

    template_name = "compose.html"
    form_class = MessageForm

    def get_initial(self):
        initial = super().get_initial()
        job = get_object_or_404(PostJob, id=self.kwargs["job_id"])
        initial["recipient"] = job.author
        return initial

    def form_valid(self, form):
        form.instance.sender = self.request.user
        job = get_object_or_404(PostJob, id=self.kwargs["job_id"])
        form.instance.recipient = job.author
        form.instance.job = job
        message = form.save(commit=False)

        if "attachment" in self.request.FILES:
            message.attachment = self.request.FILES["attachment"]
        form.save()

        return redirect("message-success")


class MessageSuccessView(DetailView):
    """Display a success message after sending a message."""

    def get(self, request, *args, **kwargs):
        return render(request, "message-success.html")


class DeleteMessageView(LoginRequiredMixin, DeleteView):
    """Soft delete a message."""

    model = Message
    template_name = "inbox.html"

    def form_valid(self, request, *args, **kwargs):
        print("DeleteMessageView is being called.")
        self.object = self.get_object()
        print(f"Retrieved message with ID: {self.object.id}")
        if (
            self.object.recipient != self.request.user
            and self.object.sender != self.request.user
        ):
            raise Http404("Chyba.")

        self.object.is_archived = True
        print(f"Setting is_archived for message ID {self.object.id}")
        self.object.save()

        return redirect("inbox")
