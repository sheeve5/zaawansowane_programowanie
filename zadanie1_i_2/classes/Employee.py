class Employee:
    first_name: str
    last_name: str
    hire_date: str
    birth_date: str
    city: str
    street: str
    zip_code: str
    phone: str

    def __str__(self):
        return "{} {}, zatrudniony/a {}, urodzony/a {}" \
               "\nAdres zamieszkania: ul {} w {}, kod pocztowy {}" \
               "\nNr telefonu: {}".format(
                self.first_name,
                self.last_name,
                self.hire_date,
                self.birth_date,
                self.street,
                self.city,
                self.zip_code,
                self.phone)

    def __init__(self, _first_name: str, _last_name: str, _hire_date: str,
                 _birth_date: str, _city: str, _street: str,
                 _zip_code: str, _phone: str):
        self.first_name = _first_name
        self.last_name = _last_name
        self.hire_date = _hire_date
        self.birth_date = _birth_date
        self.street = _street
        self.city = _city
        self.zip_code = _zip_code
        self.phone = _phone
