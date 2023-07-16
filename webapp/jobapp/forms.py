from django import forms
from django.core.exceptions import ValidationError
from jobapp.models import DrivingLicence

from .models import PostJob, Language, Position


class PostJobForm(forms.ModelForm):
    state = forms.ChoiceField(choices=Language.STATE_CHOICES)
    level = forms.ChoiceField(choices=Language.LEVEL_CHOICES)

    class Meta:
        model = PostJob
        fields = ['positions', 'info_position', 'place', 'state', 'level', 'experience', 'accommodation', 'work_type', 'salary',
                  'diet']

    def clean(self):
        cleaned_data = super().clean()
        state = cleaned_data.get('state')
        level = cleaned_data.get('level')

        if state and level:
            language, created = Language.objects.get_or_create(state=state, level=level)
            cleaned_data['language'] = language
        return cleaned_data

    def clean_driving_licence(self):
        licences = self.cleaned_data.get('driving_licence')
        valid_licences = [choice[0] for choice in DrivingLicence.CATEGORY_CHOICES]
        for licence in licences:
            if licence.licence not in valid_licences:
                raise ValidationError(f"Neplatná kategorie řidičského průkazu: {licence.licence}")
        return licences
