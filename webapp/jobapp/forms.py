from django import forms
from django.core.exceptions import ValidationError
from jobapp.models import DrivingLicence

from .models import PostJob, Language, Position, PositionCategory, Place


class PostJobForm(forms.ModelForm):
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    category = forms.ModelChoiceField(
        queryset=PositionCategory.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    place = forms.ModelChoiceField(
        queryset=Place.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    info_position = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    language = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    experience = forms.ChoiceField(
        choices=PostJob.EXPERIENCE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    accommodation = forms.ChoiceField(
        choices=PostJob.ACCOMMODATION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    work_type = forms.ChoiceField(
        choices=PostJob.WORK_TYPE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    driving_licence = forms.ModelMultipleChoiceField(
        queryset=DrivingLicence.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    salary = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(100)],
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    diet = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(100)],
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    start_date = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
    )

    class Meta:
        model = PostJob
        fields = [
            "start_date",
            "category",
            "position",
            "experience",
            "work_type",
            "place",
            "accommodation",
            "info_position",
            "language",
            "driving_licence",
            "salary",
            "diet",
        ]
