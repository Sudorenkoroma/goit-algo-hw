class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for el in self.contacts:
            if el["id"] == id:
                return el
            else:
                return None

    def remove_contacts(self, id):
        for el in self.contacts:
            if el["id"] == id:
                self.contacts.remove(el)
            else:
                return None


contact = Contacts()
contact.add_contacts("asd", 4564, "@mail", "favirite")
sol = contact.get_contact_by_id(1)

res = contact.remove_contacts(1)
rec = contact.list_contacts()
print(rec)



