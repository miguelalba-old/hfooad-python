#!/usr/bin/python3
"""
Rick's initial search application

Author: m1ge7
Date: 2014/04/04
"""


class Guitar:

    def __init__(self, serial_number, price, builder, model, type, backwood,
                 topwood):
        self._serial_number = serial_number
        self._price = price
        self._builder = builder
        self._model = model
        self._type = type
        self._backwood = backwood
        self._topwood = topwood

    def get_serial_number(self):
        return self._serial_number

    def get_price(self):
        return self._price

    def get_builder(self):
        return self._builder

    def get_model(self):
        return self._model

    def get_type(self):
        return self._type

    def get_backwood(self):
        return self._backwood

    def get_topwood(self):
        return self._topwood


class Inventory:

    def __init__(self):
        self._guitars = []

    def add_guitar(self, serial_number, price, builder, model, type, backwood,
                   topwood):
        guitar = Guitar(serial_number, price, builder, model, type, backwood,
                        topwood)
        self._guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self._guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search(self, search_guitar):
        for guitar in self._guitars:
            builder = search_guitar.get_builder()
            if builder is not None and builder != guitar.get_builder():
                continue

            model = search_guitar.get_model()
            if model is not None and model != guitar.get_model():
                continue

            type = search_guitar.get_type()
            if type is not None and type != guitar.get_type():
                continue

            backwood = search_guitar.get_backwood()
            if backwood is not None and backwood != guitar.get_backwood():
                continue

            topwood = search_guitar.get_topwood()
            if topwood is not None and topwood != guitar.get_topwood():
                continue

        return None


def initialize_inventory():
    inventory = Inventory()
    inventory.add_guitar("11277", 3999.95, "Collings", "CJ", "acoustic",
                         "Indian Rosewood", "Sitka")
    inventory.add_guitar("V95693", 1499.95, "Fender", "Stratocastor",
                         "electric", "Alder", "Alder")
    inventory.add_guitar("V9512", 1549.95, "Fender", "Stratocastor",
                         "electric", "Alder", "Alder")
    inventory.add_guitar("122784", 5495.95, "Martin", "D-18", "acoustic",
                         "Mahogany", "Adirondack")
    inventory.add_guitar("76531", 6295.95, "Martin", "OM-28", "acoustic",
                         "Brazilian Rosewood", "Adriondack")
    inventory.add_guitar("70108276", 2295.95, "Gibson", "Les Paul", "electric",
                         "Mahogany", "Maple")
    inventory.add_guitar("82765501", 1890.95, "Gibson", "SG '61 Reissue",
                         "electric", "Mahogany", "Mahogany")
    inventory.add_guitar("77023", 6275.95, "Martin", "D-28", "acoustic",
                         "Brazilian Rosewood", "Adirondack")
    inventory.add_guitar("1092", 12995.95, "Olson", "SJ", "acoustic",
                         "Indian Rosewood", "Cedar")
    inventory.add_guitar("566-62", 8999.95, "Ryan", "Cathedral", "acoustic",
                         "Cocobolo", "Cedar")
    inventory.add_guitar("6 29584", 2100.95, "PRS", "Dave Navarro Signature",
                         "electric", "Mahogany", "Maple")
    return inventory


if __name__ == '__main__':
    inventory = initialize_inventory()

    what_erin_likes = Guitar("", 0, "fender", "Stratocastor", "electric",
                             "Alder", "Alder")
    guitar = inventory.search(what_erin_likes)

    if guitar is not None:
        print("Erin, you might like this " + guitar.get_builder() + " " +
              guitar.get_model() + " " + guitar.get_type() + " guitar:\n  " +
              guitar.get_backwood() + " back and sides,\n   " +
              guitar.get_topwood() + " top.\nYou can have it for only $" +
              guitar.get_price() + "!")
    else:
        print("Sorry, Erin, we have nothing for you.")
