class Library:
    city: str
    street: str
    zip_code: str
    open_hours: str
    phone: str

    def __str__(self):
        return "Adres: ulica {}, w {}, kod pocztowy {}" \
               "\nGodziny otwarcia: {}" \
               "\nNr telefonu: {}".format(
                    self.street,
                    self.city,
                    self.zip_code,
                    self.open_hours,
                    self.phone)

    def __init__(self, _street: str, _city: str, _zip_code: str,
                 _open_hours: str, _phone: str):
        self.city = _city
        self.street = _street
        self.zip_code = _zip_code
        self.open_hours = _open_hours
        self.phone = _phone

