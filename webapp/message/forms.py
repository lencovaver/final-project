from django import forms
from message.models import Message
from users.models import User


class MessageForm(forms.ModelForm):
    """Form for composing a new message."""

    recipient = forms.ModelChoiceField(
        queryset=User.objects.all(), widget=forms.HiddenInput()
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Write your message here..."}
        )
    )
    attachment = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}), required=False
    )

    class Meta:
        model = Message
        fields = ["recipient", "content"]
