from classes.Property import Property

class House(Property):
    plot: int

    def __init__(self, _area: int, _rooms: int, _price: int,
                 _address: str, _plot: int):
        super().__init__(_area, _rooms, _price, _address)
        self.plot = _plot

    def __str__(self):
        return "Plot size: {}m2, house area: {}m2, {} rooms, " \
               "\nprice of {}$, at {}".format(
                    self.plot,
                    self.area,
                    self.rooms,
                    self.price,
                    self.address)
