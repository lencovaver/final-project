from django.test import TestCase
from unittest.mock import MagicMock

from jobapp.forms import PostJobForm
from jobapp.models import (
    Position,
    PositionCategory,
    Place,
    Language,
    DrivingLicence,
    PostJob,
)


class TestPostJobForm(TestCase):
    def setUp(self):
        # Mocking the objects.all() queryset method to return an empty queryset.
        Position.objects.all = MagicMock(return_value=Position.objects.none())
        PositionCategory.objects.all = MagicMock(
            return_value=PositionCategory.objects.none()
        )
        Place.objects.all = MagicMock(return_value=Place.objects.none())
        Language.objects.all = MagicMock(return_value=Language.objects.none())
        DrivingLicence.objects.all = MagicMock(
            return_value=DrivingLicence.objects.none()
        )

        self.form_data = {
            "position": Position(),  # an instance of Position model
            "category": PositionCategory(),  # an instance of PositionCategory model
            "place": Place(),  # an instance of Place model
            "info_position": "Info about the position",
            "language": [],  # empty queryset of Language instances
            "experience": PostJob.EXPERIENCE_CHOICES[0][
                0
            ],  # the key of first EXPERIENCE_CHOICES
            "accommodation": PostJob.ACCOMMODATION_CHOICES[0][
                0
            ],  # the key of first ACCOMMODATION_CHOICES
            "work_type": PostJob.WORK_TYPE_CHOICES[0][
                0
            ],  # the key of first WORK_TYPE_CHOICES
            "driving_licence": [],  # empty queryset of DrivingLicence instances
            "salary": "1",
            "diet": "1",
            "start_date": "2022-12-12",
        }

    def test_form_fields(self):
        form = PostJobForm(data=self.form_data)
        self.assertTrue(form.is_valid())

        # Ensure the form returned expected cleaned data
        self.assertCountEqual(form.cleaned_data.keys(), self.form_data.keys())
