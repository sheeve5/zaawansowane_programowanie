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

