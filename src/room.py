# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_tp = None
        self.items = items 

    def __str__(self):
        return f"Room Name: {self.name} Description: {self.description}"
        
    def AddToRoom(self, item):
        self.items.append(item)

    def GetRoomItems(self):
        for item in self.items:
            print(f"In this room: {item.name}")
