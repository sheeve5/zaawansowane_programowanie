import magazine.utils as utils


class Order:
    products: list
    id: int

    def function(self) -> str:
        return utils.say_hello()+" from " + self.id
