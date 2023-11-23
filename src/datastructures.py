from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # lista de ejemplo de miembros
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name" : "Jackson",
                "age" : 33,
                "lucky_Numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jone",
                "last_name" : "Jackson",
                "age" : 35,
                "lucky_Numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name" : "Jackson",
                "age" : 5,
                "lucky_Numbers": [1]
            }
        ]

    # método de solo lectura: úsalo para generar ID de miembros aleatorios al agregar miembros a la lista
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False

    def update_member(self, id, updated_member):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members[i] = updated_member
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member

    # este método está completo, devuelve una lista con todos los miembros de la familia
    def get_all_members(self):
        return self._members
