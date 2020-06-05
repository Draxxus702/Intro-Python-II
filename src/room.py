# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, loot=None, n_to=None, e_to=None, s_to=None, w_to=None):
        self.name=name
        self.description=description
        self.loot=[] if loot is None else loot
        self.connection={
            "n": n_to,
            "e": e_to,
            "s": s_to,
            "w": w_to
        }

    def __str__(self):
        return f"{self.name}, {self.description}, {self.loot}"

    def addItem(self, item):
        self.loot.append(item)

    def removeItem(self, item):
        self.loot.remove(item)