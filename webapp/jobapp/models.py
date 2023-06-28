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
    place = models.ForeignKey(Place, related_name="postjobs", on_delete=models.CASCADE)
    info_position = models.TextField()
    #language = models.ForeignKey(Language, related_name="language", on_delete=models.CASCADE)
    salary = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f"{self.positions} - {self.place} ({self.salary}CHF)"

