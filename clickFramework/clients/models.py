import uuid


class Client:
    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        # Para convertir a dict y escribir en csv
        return vars(self)

    @staticmethod
    # No recibe self porque no necesita una instacia
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']
