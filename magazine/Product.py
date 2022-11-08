import magazine.utils as utils


class Product:
    price: float
    name: str
    id: int

    def function(self) -> str:
        return utils.say_hello()+" from " + self.name
