"""
Rick's search application final version (encapsulated guitar spec comparison)

Author: m1ge7
Date: 2014/04/13
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
    UNSPECIFIED = 2

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
    def __init__(self, serial_number, price, spec):
        self._serial_number = serial_number
        self._price = price
        self._spec = spec

    def get_serial_number(self):
        return self._serial_number

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_spec(self):
        return self._spec


class GuitarSpec:

    def __init__(self, builder, model, type, num_strings, backwood, topwood):
        self._builder = builder
        self._model = model
        self._type = type
        self._num_strings = num_strings
        self._backwood = backwood
        self._topwood = topwood

    def get_builder(self):
        return self._builder

    def get_model(self):
        return self._model

    def get_type(self):
        return self._type

    def get_num_strings(self):
        return self._num_strings

    def get_backwood(self):
        return self._backwood

    def get_topwood(self):
        return self._topwood

    def __eq__(self, other_spec):
        if self._builder != other_spec.get_builder():
            return False
        if (self._model is not None and
            self._model.lower() != other_spec.get_model().lower()):
            return False
        if self._type != other_spec.get_type():
            return False
        if self._num_strings != other_spec.get_num_strings():
            return False
        if self._backwood != other_spec.get_backwood():
            return False
        if self._topwood != other_spec.get_topwood():
            return False
        return True


class Inventory:

    def __init__(self):
        self._guitars = []

    def add_guitar(self, serial_number, price, spec):
        guitar = Guitar(serial_number, price, spec)
        self._guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self._guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search(self, search_spec):
        matching_guitars = []
        for guitar in self._guitars:
            if guitar.get_spec() == search_spec:
                matching_guitars.append(guitar)
        return matching_guitars


def initialize_inventory():
    inv = Inventory()
    inv.add_guitar("11277", 3999.95, GuitarSpec(Builder.COLLINGS, "CJ",
        Type.ACOUSTIC, 6, Wood.INDIAN_ROSEWOOD, Wood.SITKA))
    inv.add_guitar("V95693", 1499.95, GuitarSpec(Builder.FENDER, "Stratocastor",
                Type.ELECTRIC, 6, Wood.ALDER, Wood.ALDER))
    inv.add_guitar("V9512", 1549.95, GuitarSpec(Builder.FENDER, "Stratocastor",
                Type.ELECTRIC, 6, Wood.ALDER, Wood.ALDER))
    inv.add_guitar("122784", 5495.95, GuitarSpec(Builder.MARTIN, "D-18",
                Type.ACOUSTIC, 6, Wood.MAHOGANY, Wood.ADIRONDACK))
    inv.add_guitar("76531", 6295.95, GuitarSpec(Builder.MARTIN, "OM-28",
                Type.ACOUSTIC, 6, Wood.BRAZILIAN_ROSEWOOD,
                Wood.ADIRONDACK))
    inv.add_guitar("70108276", 2295.95, GuitarSpec(Builder.GIBSON, "Les Paul",
                Type.ELECTRIC, 6, Wood.MAHOGANY, Wood.MAHOGANY))
    inv.add_guitar("82765501", 1890.95, GuitarSpec(Builder.GIBSON, "SG '61 Reissue",
                Type.ELECTRIC, 6, Wood.MAHOGANY, Wood.MAHOGANY))
    inv.add_guitar("77023", 6275.95, GuitarSpec(Builder.MARTIN, "D-28",
                Type.ACOUSTIC, 12, Wood.BRAZILIAN_ROSEWOOD,
                Wood.ADIRONDACK))
    inv.add_guitar("1092", 12995.95, GuitarSpec(Builder.OLSON, "SJ", Type.ACOUSTIC,
                12, Wood.COCOBOLO, Wood.CEDAR))
    inv.add_guitar("6 29584", 2100.95, GuitarSpec(Builder.PRS,
        "Dave Navarro Signature", Type.ELECTRIC, 6,
        Wood.MAHOGANY, Wood.MAPLE))
    return inv


if __name__ == '__main__':
    inventory = initialize_inventory()

    what_erin_likes = GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC,
                                 6, Wood.ALDER, Wood.ALDER)
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

