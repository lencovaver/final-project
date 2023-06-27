from django.db import models


class Position(models.Model):
    name_position = models.CharField(max_length=100)

    def __repr__(self):
        return f"{self.name_position}"

    def __str__(self):
        return repr(self)

#class Language(models.Model):
    #name_language = models.CharField(max_length=200)

    #def __str__(self):  # specialni metoda pro zobrazovani nazvů zemí
        #return self.name

class Place(models.Model):
    name_place = models.CharField(max_length=100)
    shortname = models.CharField(max_length=3)

    def __repr__(self):
        return f"{self.name_place}"

    def __str__(self):
        return repr(self)
class PostJob(models.Model):

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    positions = models.ForeignKey(Position,related_name="position", on_delete=models.CASCADE)
    info_position = models.TextField()
    #language = models.ForeignKey(Language, related_name="language", on_delete=models.CASCADE)
    salary = models.IntegerField()
    status = models.BooleanField()
    place = models.ForeignKey(Place,related_name="postjobs", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.positions} - {self.place}"