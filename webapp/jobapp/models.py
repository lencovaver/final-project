from django.db import models


class PositionCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Position Categories"

    def __str__(self):
        return self.name


class Position(models.Model):
    name_position = models.CharField(max_length=100)
    category = models.ForeignKey(
        PositionCategory, on_delete=models.CASCADE, blank=False
    )

    def __str__(self):
        return self.name_position


class Place(models.Model):
    name_place = models.CharField(max_length=100)
    shortname = models.CharField(max_length=3)

    class Meta:
        ordering = ["name_place"]

    def __str__(self):
        return self.name_place


class Language(models.Model):
    STATE_CHOICES = [
        ("ENG", "🇬🇧 angličtina"),
        ("CHF", "🇨🇭 švýcarská němčina"),
        ("DEU", "🇩🇪 němčina"),
        ("FRA", "🇫🇷 francouzština"),
        ("ITA", "🇮🇹 italština"),
    ]
    LEVEL_CHOICES = [
        ("1", "A1 - začátečník"),
        ("2", "A2 - pokročilý začátečník"),
        ("3", "B1 - mírně pokročilý"),
        ("4", "B2 - středně pokročilý"),
        ("5", "C1 - velmi pokročilý"),
        ("6", "C2 - expert"),
    ]
    state = models.CharField(max_length=3, choices=STATE_CHOICES, default="ENG")
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default="1")

    def get_language_display(self):
        for state in Language.STATE_CHOICES:
            if state[0] == self.state:
                return state[1]

    def get_level_display(self):
        for level in Language.LEVEL_CHOICES:
            if level[0] == self.level:
                return level[1]

    def __str__(self):
        return f"{self.get_language_display()} - {self.get_level_display()}"


class DrivingLicence(models.Model):
    licence_category = models.CharField(max_length=6, default="")

    def __str__(self):
        return self.licence_category


class PostJob(models.Model):
    EXPERIENCE_CHOICES = [
        ("1-3 roky", "1-3"),
        ("4-6 let", "4-6"),
        ("6-9 let", "6-9"),
        ("10 a více let", "10 a více"),
    ]
    ACCOMMODATION_CHOICES = [
        ("vlastní ubytování", "mám zajištěné"),
        ("zajištěné ubytování", "chci zajistit"),
    ]
    STATUS_CHOICES = [
        ("active", "Aktivní"),
        ("archived", "Archivovaný"),
    ]
    WORK_TYPE_CHOICES = [
        ("plný", "Plný úvazek"),
        ("částečný", "Částečný úvazek"),
        ("brigáda", "Brigáda"),
    ]
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, default="")
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.ForeignKey(
        Position, related_name="position", on_delete=models.CASCADE
    )
    driving_licence = models.ManyToManyField(DrivingLicence, blank=True)
    experience = models.CharField(
        max_length=100, choices=EXPERIENCE_CHOICES, default="1-3"
    )
    place = models.ForeignKey(
        Place, related_name="postjobs", on_delete=models.CASCADE, null=True
    )
    language = models.ManyToManyField(Language, related_name="language", blank=True)
    accommodation = models.CharField(
        max_length=30, choices=ACCOMMODATION_CHOICES, default=""
    )
    info_position = models.TextField()
    work_type = models.CharField(max_length=10, choices=WORK_TYPE_CHOICES, default="")
    salary = models.IntegerField(default=30)
    diet = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")
    start_date = models.DateField()

    def __str__(self):
        return self.position.name_position
