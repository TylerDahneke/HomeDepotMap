import aisle
import item
import file_management


class store:

    def __init__(self):
        self.aisles = [None]
        self.num_of_aisles = 0

    def add_aisle(self, inp):
        self.aisles.append(inp)
        self.num_of_aisles += 1

    def get_item_from_aisle(self, inp):
        return self.aisles[inp.numb]
