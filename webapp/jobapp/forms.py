from django import forms
from django.core.exceptions import ValidationError
from jobapp.models import DrivingLicence

from .models import PostJob, Language, Position, PositionCategory, Place


class PostJobForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=PositionCategory.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    info_position = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    place = forms.ModelChoiceField(
        queryset=Place.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    state = forms.ChoiceField(
        choices=Language.STATE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    level = forms.ChoiceField(
        choices=Language.LEVEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    experience = forms.ChoiceField(
        choices=PostJob.EXPERIENCE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    accommodation = forms.ChoiceField(
        choices=PostJob.ACCOMMODATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    work_type = forms.ChoiceField(
        choices=PostJob.WORK_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    driving_licence = forms.ChoiceField(
        choices=lambda: [(licence.id, licence.short_name) for licence in DrivingLicence.objects.all()],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    salary = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(100)],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    diet = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(100)],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    start_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
    )

    class Meta:
        model = PostJob
        fields = ['category', 'position', "info_position", 'place', 'state', 'level',
                  'experience', 'accommodation', 'work_type', "driving_licence", 'salary',
                  'diet', "start_date"]

    def clean(self):
        cleaned_data = super().clean()
        state = cleaned_data.get('state')
        level = cleaned_data.get('level')

        #if state and level:
        #    language, created = Language.objects.get_or_create(state=state, level=level)
        #    cleaned_data['language'] = language
        #return cleaned_data

