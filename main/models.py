from django.db import models
from django.core.exceptions import ValidationError

class SpyCat(models.Model):
    name = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    breed = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Mission(models.Model):
    cat = models.ForeignKey(SpyCat, related_name="missions", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Mission for {self.cat.name}"

    def delete(self, *args, **kwargs):
        if self.cat:
            raise ValidationError("Не можна видалити місію, яка призначена коту.")
        super().delete(*args, **kwargs)


class Target(models.Model):
    mission = models.ForeignKey(Mission, related_name="targets", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    notes = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
