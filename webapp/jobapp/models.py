from django.db import models


class Position(models.Model):
    name_position = models.CharField(max_length=100)

    class Meta:
        ordering = ['name_position']

    def __str__(self):
        return self.name_position


class Place(models.Model):
    name_place = models.CharField(max_length=100)
    shortname = models.CharField(max_length=3)

    class Meta:
        ordering = ['name_place']

    def __str__(self):
        return self.name_place


class Language(models.Model):
    STATE_CHOICES = [
        ('ENG', '🇬🇧 angličtina'),
        ('CHF', '🇨🇭 švýcarská němčina'),
        ('DEU', '🇩🇪 němčina'),
        ('FRA', '🇫🇷 francouzština'),
        ('ITA', '🇮🇹 italština'),
    ]
    LEVEL_CHOICES = [
        ('1', 'A1 - začátečník'),
        ('2', 'A2 - pokročilý začátečník'),
        ('3', 'B1 - mírně pokročilý'),
        ('4', 'B2 - středně pokročilý'),
        ('5', 'C1 - velmi pokročilý'),
        ('6', 'C2 - expert'),
    ]
    state = models.CharField(max_length=3, choices=STATE_CHOICES, default="ENG")
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default="1")

    def get_level_name(self):
        for level in self.LEVEL_CHOICES:
            if level[0] == self.level:
                return level[1]

    def __str__(self):
        return f"{self.state} - {self.get_level_name()}"


class DrivingLicence(models.Model):
    CATEGORY_CHOICES = [
        ('', '---------'),
        ('AM', 'AM 🛵'),
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A', 'A 🏍️'),
        ('B1', 'B1 🚚'),
        ('B', 'B 🚗'),
        ('C1', 'C1 🚛'),
        ('C', 'C'),
        ('D1', 'D1 🚐'),
        ('D', 'D 🚌'),
        ('BE', 'BE '),
        ('C1E', 'C1E'),
        ('CE', 'CE'),
        ('D1E', 'D1E'),
        ('DE', 'DE'),
        ('T', 'T 🚜')
    ]

    licence = models.CharField(max_length=6, choices=CATEGORY_CHOICES, blank=True)

    def __str__(self):
        return self.licence


class PostJob(models.Model):
    EXPERIENCE_CHOICES = [
        ('1-3 roky', '1-3'),
        ('4-6 let', '4-6'),
        ('6-9 let', '6-9'),
        ('10 a více let', '10 a více'),
    ]
    ACCOMMODATION_CHOICES = [
        ('vlastní ubytování', 'vlastní'),
        ('zajištěné ubytování', 'zajištěné'),
    ]
    STATUS_CHOICES = [
        ("active", "Aktivní"),
        ("archived", "Archivovaný"),
    ]
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, default='')
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    positions = models.ForeignKey(Position, related_name="position", on_delete=models.CASCADE)
    driving_licence = models.ManyToManyField(DrivingLicence, blank=True)
    experience = models.CharField(max_length=100, choices=EXPERIENCE_CHOICES, default='1-3')
    place = models.ForeignKey(Place, related_name="postjobs", on_delete=models.CASCADE, null=True)
    language = models.ManyToManyField(Language, related_name="language")
    accommodation = models.CharField(max_length=30, choices=ACCOMMODATION_CHOICES, default='')
    info_position = models.TextField()
    salary = models.IntegerField(choices=[(i, i) for i in range(100)], default=30)
    diet = models.IntegerField(choices=[(i, i) for i in range(31)], default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")

    def __str__(self):
        return self.positions.name_position
