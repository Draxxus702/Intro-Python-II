# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name=name
        self.current_room=current_room
        self.inventory=[] if inventory is None else inventory

    def __str__(self):
        return f"{self.name}, {self.current_room}, {self.inventory}"

    def move(self, direction):
        if self.current_room.connection[direction] is not None:
            self.current_room=self.current_room.connection[direction]
        else:
            print("You may not go that way")

    def pickUpItem(self, item):
        self.inventory.append(item)

    def dropItem(self, item):
        self.inventory.remove(item)


   