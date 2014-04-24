"""
Rick's highly cohesive search application

Author: m1ge7
Date: 2014/04/24
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
class InstrumentType(enum.Enum):
    GUITAR = 0
    BANJO = 1
    DOBRO = 2
    FIDDLE = 3
    BASS = 4
    MANDOLIN = 5
    UNSPECIFIED = 6

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


@enum.unique
class Style(enum.Enum):
    A = 0
    F = 1

    def __str__(self):
        if self.name == 'A':
            return "A style"
        elif self.name == 'F':
            return "F style"
        else:
            return "Unspecified"


class Inventory:

    def __init__(self):
        self._inventory = []

    def add_instrument(self, serial_number, price, spec):
        instrument = Instrument(serial_number, price, spec)
        self._inventory.append(instrument)

    def get(self, serial_number):
        for instrument in self._inventory:
            if instrument.get_serial_number() == serial_number:
                return instrument
        return None

    def search(self, search_spec):
        return [instrument for instrument in self._inventory
                if instrument.get_spec() == search_spec]


class Instrument:

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


class InstrumentSpec(dict):

    def __init__(self, properties=None):
        if properties is None:
            super(InstrumentSpec, self).__init__()
        else:
            super(InstrumentSpec, self).__init__(properties)

    def __eq__(self, spec):
        for key, value in spec.items():
            if not key in self.keys():
                return False
            if value != self[key]:
                return False
        return True


class FindInstrumentTester:

    def main(self):
        inventory = Inventory()
        self.initialize_inventory(inventory)

        properties = {}
        properties['builder'] = Builder.GIBSON
        properties['back_wood'] = Wood.MAPLE
        what_bryan_likes = InstrumentSpec(properties)

        matching_instruments = inventory.search(what_bryan_likes)
        if matching_instruments:
            print("Bryan, you might like these instruments:")
            for instrument in matching_instruments:
                spec = instrument.get_spec()
                print("We have a " + str(spec['instrument_type']) +
                        " with the following properties")
                for key, value in spec.items():
                    if key == 'instrument_type':
                        continue
                    print("    " + str(key) + ": " +  str(value))
                print("  You can have this " + str(spec['instrument_type']) + 
                        str(instrument.get_price()) + "\n---")
        else:
            print("Sorry, Bryan, we have nothing for you.")

    def initialize_inventory(self, inventory):
        properties = dict()
        properties['instrument_type'] = InstrumentType.GUITAR
        properties['builder'] = Builder.COLLINGS
        properties['model'] = 'CJ'
        properties['type'] = Type.ACOUSTIC
        properties['num_strings'] = 6
        properties['top_wood'] = Wood.INDIAN_ROSEWOOD
        properties['back_wood'] =Wood.SITKA
        inventory.add_instrument("11277", 3999.95, InstrumentSpec(properties))

        properties['builder'] = Builder.MARTIN
        properties['model'] = 'D-18'
        properties['top_wood'] = Wood.MAHOGANY
        properties['back_wood'] = Wood.ADIRONDACK
        inventory.add_instrument('122784', 5495.95, InstrumentSpec(properties))

        properties['builder'] = Builder.FENDER
        properties['model'] = 'Stratocastor'
        properties['type'] = Type.ELECTRIC
        properties['top_wood'] = Wood.ALDER
        properties['back_wood'] = Wood.ALDER
        inventory.add_instrument('V95693', 1499.95, InstrumentSpec(properties))
        inventory.add_instrument('V9512', 1549.95, InstrumentSpec(properties))

        properties['builder'] = Builder.GIBSON
        properties['model'] = 'Les Paul'
        properties['top_wood'] = Wood.MAPLE
        properties['back_wood'] = Wood.MAPLE
        inventory.add_instrument('70108276', 2295.95, InstrumentSpec(properties))

        properties['model'] = "SG '61 Reissue"
        properties['top_wood'] = Wood.MAHOGANY
        properties['back_wood'] = Wood.MAHOGANY
        inventory.add_instrument('82765501', 1890.95, InstrumentSpec(properties))

        properties['instrument_type'] = InstrumentType.MANDOLIN
        properties['type'] = Type.ACOUSTIC
        properties['model'] = 'F-5G'
        properties['back_wood'] = Wood.MAPLE
        properties['top_wood'] = Wood.MAPLE
        properties.pop('num_strings')
        inventory.add_instrument('9019920', 5495.99, InstrumentSpec(properties))

        properties['instrument_type'] = InstrumentType.BANJO
        properties['model'] = 'RB-3 Wreath'
        properties.pop('top_wood')
        properties['num_strings'] = 5
        inventory.add_instrument('8900231', 2945.95, InstrumentSpec(properties))


if __name__ == '__main__':
    tester = FindInstrumentTester()
    tester.main()
