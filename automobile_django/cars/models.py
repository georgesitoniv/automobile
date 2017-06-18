import uuid
from django.db import models

def get_slot_number():
    return (Car.objects.count() + 1)

class Color(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    color = models.ForeignKey(Color, related_name="cars")
    slot_number = models.IntegerField(
        null=True,
        blank=True,
        default=get_slot_number
    )

    def __str__(self):
        return self.name
