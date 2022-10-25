class Property:
    area: int
    rooms: int
    price: int
    address: str

    def __init__(self, _area: int, _rooms: int, _price: int, _address: str):
        self.area = _area
        self.rooms = _rooms
        self.price = _price
        self.address = _address


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


flat = Flat(80, 4, 200000, "ul Ul, Warszawa", 5)
house = House(300, 15, 1000000, "ul Ul, Warszawa", 1000)

print(flat)
print(house)
