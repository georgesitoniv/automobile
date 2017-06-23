
import uuid
from django.db import models
from ordered_model.models import OrderedModel

def get_slot_number():
    return (Car.objects.count() + 1)

class OrderUpdateQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        super(OrderUpdateQuerySet, self).delete(*args, **kwargs)
        self.update_car_order()

    def update_car_order(self):
        cars = Car.objects.order_by('order')
        for index, car in enumerate(cars):
            car.order = index
            car.save()

class BaseObject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        unique=True
        )
    objects = OrderUpdateQuerySet.as_manager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        super(BaseObject, self).delete(*args, **kwargs)
        self.objects.update_car_order()

class Color(BaseObject):
    pass

class Car(OrderedModel, BaseObject):
    color = models.ForeignKey(
        Color,
        related_name="cars",
        on_delete=models.CASCADE
        )

    class Meta:
        ordering = ('order', )
