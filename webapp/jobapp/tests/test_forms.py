from django.test import TestCase
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
    @classmethod
    def setUpTestData(cls):
        cls.position = Position.objects.create(name="Test Position")
        cls.category = PositionCategory.objects.create(name="Test Category")
        cls.place = Place.objects.create(name="Test Place")
        cls.language = Language.objects.create(name="Test Language")
        cls.driving_licence = DrivingLicence.objects.create(name="Test Licence")

    def test_form_valid(self):
        form = PostJobForm(
            data={
                "position": self.position.id,
                "category": self.category.id,
                "place": self.place.id,
                "info_position": "Test information",
                "language": [self.language.id],
                "experience": PostJob.EXPERIENCE_CHOICES[0][0],
                "accommodation": PostJob.ACCOMMODATION_CHOICES[0][0],
                "work_type": PostJob.WORK_TYPE_CHOICES[0][0],
                "driving_licence": [self.driving_licence.id],
                "salary": "50",
                "diet": "30",
                "start_date": "2023-02-20",
            }
        )

        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = PostJobForm(data={})

        self.assertFalse(form.is_valid())
