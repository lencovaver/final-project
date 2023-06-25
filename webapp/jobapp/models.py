from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=3)

    def __repr__(self):
        return f"Place ({self.pk}) - [{self.shortname}] {self.name}"

    def __str__(self):
        return repr(self)
class PostJob(models.Model):

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    positions = models.TextField()
    info_position = models.TextField()
    #language = models.CharField(choices=LANGUAGE_CHOICES, max_length=100)
    salary = models.IntegerField()
    status = models.BooleanField()
    place = models.ForeignKey(Place,related_name="postjobs", on_delete=models.CASCADE)

