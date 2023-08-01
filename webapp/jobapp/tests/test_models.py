from django.test import TestCase
from django.contrib.auth import get_user_model
from jobapp.models import (
    PostJob,
    Position,
    Place,
    Language,
    DrivingLicence,
    PositionCategory,
)

User = get_user_model()


class PostJobModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

        self.language = Language.objects.create(state="ENG")
        self.category = PositionCategory.objects.create(name="TestCategory")

        self.position = Position.objects.create(
            name_position="testPosition", category=self.category
        )
        self.place = Place.objects.create(name_place="TestPlace")
        self.driving_licence = DrivingLicence.objects.create(
            licence_category="Test Licence"
        )

        self.post_job = PostJob.objects.create(
            author=self.user,
            position=self.position,
            place=self.place,
            experience="1-3 roky",
            accommodation="vlastní ubytování",
            info_position="This is test info_position",
            work_type="plný",
            status="active",
            salary=50000,
            diet=500,
            start_date="2023-04-01",
        )
        self.post_job.language.add(self.language)
        self.post_job.driving_licence.add(self.driving_licence)

    def test_post_job_creation(self):
        self.assertEquals(self.post_job.author, self.user)
        self.assertEquals(self.post_job.position, self.position)
        self.assertEquals(self.post_job.place, self.place)
        self.assertEquals(self.post_job.experience, "1-3 roky")
        self.assertEquals(self.post_job.accommodation, "vlastní ubytování")
        self.assertEquals(self.post_job.info_position, "This is test info_position")
        self.assertEquals(self.post_job.work_type, "plný")
        self.assertEquals(self.post_job.status, "active")
        self.assertEquals(self.post_job.salary, 50000)
        self.assertEquals(self.post_job.diet, 500)
        self.assertEquals(str(self.post_job.start_date), "2023-04-01")
        self.assertIn(self.language, self.post_job.language.all())
        self.assertIn(self.driving_licence, self.post_job.driving_licence.all())
