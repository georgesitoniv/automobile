import graphene
from .types import CarType, ColorType
from cars.models import Car, Color

class MoveCarSlot(graphene.Mutation):
    """
    Moves car slot number up or down. Requires the id of the car being moved
    and the direction of the movement. The direction must be a postive or a
    negative integer.
    """
    class Input:
        id = graphene.ID()
        direction = graphene.Int()
    car = graphene.Field(CarType)

    @staticmethod
    def mutate(root, args, context, info):
        id = args.get('id')
        direction = args.get('direction')

        car = Car.objects.get(id=id)
        if direction < 0:
            car.up()
        else:
            car.down()
        return MoveCarSlot(car=car)

class MoveCarSlotExplicit(graphene.Mutation):
    """
    Moves car at a scpecific slot number. Requires the id of the car being
    moved and the desired slot number.
    """
    class Input:
        id = graphene.ID()
        slot_number = graphene.Int()

    car = graphene.Field(CarType)
    validation_error = graphene.String()

    @staticmethod
    def mutate(root, args, context, info):
        id = args.get('id')
        slot_number = args.get('slot_number')

        car = Car.objects.get(id=id)
        if slot_number >= 0:
            if slot_number <= (Car.objects.count() - 1):
                car.to(slot_number)
                return MoveCarSlotExplicit(car=car)
            else:
                return MoveCarSlotExplicit(
                    validation_error=
                        "Desired slot number execeeded current slot numbers"
                        )
