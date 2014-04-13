"""
Rick's search application with support for mandolins

Author: m1ge7
Date: 2014/04/13
"""

import enum
from abc import ABCMeta


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


class InstrumentSpec(ABCMeta):

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

    def __eq__(self, spec):
        if self._builder != spec.get_builder():
            return False
        if self._model is not None and self._model != spec.get_model():
            return False
        if self._type != spec.get_type():
            return False
        if self._backwood != spec.get_backwood():
            return False
        if self._topwood != spec.get_topwood():
            return False
        return True


class GuitarSpec(InstrumentSpec):

    def __init__(self, builder, model, type, num_strings, backwood, topwood):
        super(GuitarSpec, self).__init__(builder, model, type, backwood,
                topwood)
        self._num_strings = num_strings

    def get_num_strings(self):
        return self._num_strings

    def __eq__(self, spec):
        if (super(GuitarSpec, self).__eq__(spec) is False):
            return False
        if self._num_strings != spec.get_num_strings():
            return False
        return True


class MandolinSpec(InstrumentSpec):
    
    def __init__(self, builder, model, type, style, backwood, topwood):
        super(MandolinSpec, self).__init__(builder, model, type, backwood,
                topwood)
        self._style = style

    def get_style(self):
        return self._style

    def __eq__(self, spec):
        if super(MandolinSpec, self).__eq__(spec) is False:
            return False
        if self._style != spec.get_style():
            return False
        return True


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


class Guitar(Instrument):

    def __init__(self, serial_number, price, spec):
        super(Guitar, self).__init__(serial_number, price, spec)


class Mandolin(Instrument):

    def __init__(self, serial_number, price, spec):
        super(Mandolin, self).__init__(serial_number, price, spec)


class Inventory:

    def __init__(self):
        self._inventory = []

    def add_instrument(self, serial_number, price, spec):
        if isinstance(spec, GuitarSpec):
            instrument = Guitar(serial_number, price, spec)
        elif isinstance(spec, MandolinSpec):
            instrument = Mandolin(serial_number, price, spec)
        self._inventory.append(instrument)

    def get(self, serial_number):
        for instrument in self._inventory:
            if instrument.get_serial_number() == serial_number:
                return instrument
        return None

    def search(self, search_spec):
        return [instrument for instrument in self._inventory
                if instrument.get_spec() == search_spec]
