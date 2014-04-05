"""
Rick's search application with guitar specs (encapsulation)

Author: m1ge7
Date: 2014/04/05
"""
import enum


@enum.unique
class Builder(enum.Enum):
    FENDER = 0
    MARTIN = 1
    GIBSON = 2
    COLLINGS = 3
    OLSON = 4
    RYAN = 5
    PRS = 6
    ANY = 7

    def __str__(self):
        return self.name


@enum.unique
class Type(enum.Enum):
    ACOUSTIC = 0
    ELECTRIC = 1

    def __str__(self):
        return self.name


@enum.unique
class Wood(enum.Enum):
    INDIAN_ROSEWOOD = 0
    BRAZILIAN_ROSEWOOD = 1
    MAHOGANY = 2
    MAPLE = 3
    COCOBOLO = 4
    CEDAR = 5
    ADIRONDACK = 6
    ALDER = 7
    SITKA = 8
    UNSPECIFIED = 9

    def __str__(self):
        return self.name


class Guitar:

    def __init__(self, serial_number, price, builder, model, type, backwood,
                 topwood):
        self._serial_number = serial_number
        self._price = price
        self._spec = GuitarSpec(builder, model, type, backwood, topwood)

    def get_serial_number(self):
        return self._serial_number

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_spec(self):
        return self._spec


class GuitarSpec:

    def __init__(self, builder, model, type, backwood, topwood):
        self._builder = builder
        self._model = model
        self._type = type
        self._backwood = backwood
        self._topwood = topwood

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

    def search(self, search_spec):
        matching_guitars = []
        for guitar in self._guitars:
            guitar_spec = guitar.get_spec()
            if search_spec.get_builder() != guitar_spec.get_builder():
                continue
            model = search_spec.get_model().lower()
            if model is not None and model != guitar_spec.get_model().lower():
                continue
            if search_spec.get_type() != guitar_spec.get_type():
                continue
            if search_spec.get_backwood() != guitar_spec.get_backwood():
                continue
            if search_spec.get_topwood() != guitar_spec.get_topwood():
                continue
            matching_guitars.append(guitar)
        return matching_guitars


def initialize_inventory():
    inventory = Inventory()
    inventory.add_guitar("11277", 3999.95, Builder.COLLINGS, "CJ",
                         Type.ACOUSTIC, Wood.INDIAN_ROSEWOOD, Wood.SITKA)
    inventory.add_guitar("V95693", 1499.95, Builder.FENDER, "Stratocastor",
                         Type.ELECTRIC, Wood.ALDER, Wood.ALDER)
    inventory.add_guitar("V9512", 1549.95, Builder.FENDER, "Stratocastor",
                         Type.ELECTRIC, Wood.ALDER, Wood.ALDER)
    inventory.add_guitar("122784", 5495.95, Builder.MARTIN, "D-18",
                         Type.ACOUSTIC, Wood.MAHOGANY, Wood.ADIRONDACK)
    inventory.add_guitar("76531", 6295.95, Builder.MARTIN, "OM-28",
                         Type.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD,
                         Wood.ADIRONDACK)
    inventory.add_guitar("70108276", 2295.95, Builder.GIBSON, "Les Paul",
                         Type.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY)
    inventory.add_guitar("82765501", 1890.95, Builder.GIBSON, "SG '61 Reissue",
                         Type.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY)
    inventory.add_guitar("77023", 6275.95, Builder.MARTIN, "D-28",
                         Type.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD,
                         Wood.ADIRONDACK)
    inventory.add_guitar("1092", 12995.95, Builder.OLSON, "SJ", Type.ACOUSTIC,
                         Wood.COCOBOLO, Wood.CEDAR)
    inventory.add_guitar("6 29584", 2100.95, Builder.PRS,
                         "Dave Navarro Signature", Type.ELECTRIC,
                         Wood.MAHOGANY, Wood.MAPLE)
    return inventory


if __name__ == '__main__':
    inventory = initialize_inventory()

    what_erin_likes = GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC,
                                 Wood.ALDER, Wood.ALDER)
    matching_guitars = inventory.search(what_erin_likes)

    if matching_guitars:
        print("Erin, you might like these guitars:")
        for guitar in matching_guitars:
            spec = guitar.get_spec()
            print(" We have a " + str(spec.get_builder()) + " " +
                  str(spec.get_model()) + " " +
                  str(spec.get_type()) + " guitar:\n    " +
                  str(spec.get_backwood()) + " back and sides,\n    " +
                  str(spec.get_topwood()) +
                  " top.\n You can have if for only $" +
                  str(guitar.get_price()) + "!\n ----")
    else:
        print("Sorry, Erin, we have nothing for you.")
