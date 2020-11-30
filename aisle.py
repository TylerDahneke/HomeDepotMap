from heap import *
import item


class aisle:

    def __init__(self, numb, disc=None):
        self.numb = numb
        self.disc = disc
        self.items = MaxHeap()

    def __eq__(self, other):
        return self.numb == other.numb

    def add_item(self, item_key, disc=None):
        new_item = item.item(item_key, disc)
        self.items.enqueue(new_item)

    def get_items(self):
        return self.items.contents()


def main():
    pass

if __name__ == '__main__':
    main()