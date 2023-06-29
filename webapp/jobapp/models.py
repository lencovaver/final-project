from django.db import models


class Position(models.Model):
    name_position = models.CharField(max_length=100)

    class Meta:
        ordering = ['name_position']

    def __repr__(self):
        return f"{self.name_position}"

    def __str__(self):
        return repr(self)


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
        ('ENG1', '🇬🇧 english/beginner'),
        ('ENG2', '🇬🇧 english/advanced'),
        ('ENG3', '🇬🇧 english/native speaker'),
        ('CHF1', '🇨🇭 swiss german/beginner'),
        ('CHF2', '🇨🇭 swiss german/advanced'),
        ('CHF3', '🇨🇭 swiss german/native speaker'),
        ('DEU1', '🇩🇪 germany/beginner'),
        ('DEU2', '🇩🇪 germany/advanced'),
        ('DEU3', '🇩🇪 germany/native speaker'),
        ('FRA1', '🇫🇷 french/beginner'),
        ('FRA2', '🇫🇷 french/advanced'),
        ('FRA3', '🇫🇷 french/native speaker'),
        ('ITA1', '🇮🇹 italy/beginner'),
        ('ITA2', '🇮🇹 italy/advanced'),
        ('ITA3', '🇮🇹 italy/native speaker'),
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
    place = models.ForeignKey(Place, related_name="postjobs", on_delete=models.CASCADE)
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='NO')
    info_position = models.TextField()
    salary = models.IntegerField(choices=[(i, i) for i in range(100)], default=30)
    diet = models.IntegerField(choices=[(i, i) for i in range(31)], default=0)


    def __str__(self):
        return f"{self.positions} - {self.place} ({self.salary}CHF + spessen {self.diet}CHF)"

