from classes.Property import Property

class Flat(Property):
    floor: int

    def __init__(self, _area: int, _rooms: int, _price: int,
                 _address: str, _floor: int):
        super().__init__(_area, _rooms, _price, _address)
        self.floor = _floor

    def __str__(self):
        return "Flat area: {}m2, {} rooms, located on {} floor, " \
               "\nprice of {}$, at {}".format(
                    self.area,
                    self.rooms,
                    self.floor,
                    self.price,
                    self.address)
