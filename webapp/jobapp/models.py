from django.db import models


class Position(models.Model):
    name_position = models.CharField(max_length=100)

    class Meta:
        ordering = ['name_position']

    def __repr__(self):
        return self.name_position

    def __str__(self):
        return self.name_position

class Place(models.Model):
    name_place = models.CharField(max_length=100)
    shortname = models.CharField(max_length=3)

    class Meta:
        ordering = ['name_place']

    def __repr__(self):
        return f"{self.name_place}"

    def __str__(self):
        return repr(self)

class PostJob(models.Model):
    EXPERIENCE_CHOICES = [
        ('1-3', '1-3'),
        ('4-6', '4-6'),
        ('6-9', '6-9'),
        ('10+', '10 a více'),
    ]
    LANGUAGE_CHOICES = [
        ('NO', 'žádný'),
        ('ENG', '🇬🇧 angličtina'),
        ('CHF', '🇨🇭 švýcarská němčina'),
        ('DEU', '🇩🇪 němčina'),
        ('FRA', '🇫🇷 francouzština'),
        ('ITA', '🇮🇹 italština'),
    ]

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    positions = models.ForeignKey(Position, related_name="position", on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True, null=True, choices=[

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
    ])


    experience = models.CharField(max_length=100, choices=EXPERIENCE_CHOICES, default='1-3')
    place = models.ForeignKey(Place, related_name="postjobs", on_delete=models.CASCADE, null=True)
    language = models.ManyToManyField(Language, blank=True)
    accommodation = models.CharField(max_length=30, choices=ACCOMMODATION_CHOICES, default='')
    info_position = models.TextField()
    salary = models.IntegerField(choices=[(i, i) for i in range(100)], default=30)
    diet = models.IntegerField(choices=[(i, i) for i in range(31)], default=0)

    def __str__(self):
        return self.positions.name_position


    def clean(self):
        if self.driving_licence:
            choices = [choice[0] for choice in DrivingLicence.CATEGORY_CHOICES]
            selected_choices = self.driving_licence.values_list('licence', flat=True)
            for choice in selected_choices:
                if choice not in choices:
                    raise ValidationError(f"Neplatná kategorie: {choice}")

