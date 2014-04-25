"""
Gary's basic Game System Framework

Author: m1ge7
Date: 2014/04/25
"""

import unittest


class Unit:
    def __init__(self, id):
        self._id = id
        self._type = ""
        self._name = ""
        self._weapons = []
        self._properties = {}

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_weapons(self):
        return self._weapons

    def get_id(self):
        return self._id

    def add_weapon(self, weapon):
        self._weapons.append(weapon)

    def set_property(self, property, value):
        self._properties[property] = value

    def get_property(self, property):
        return self._properties[property]


class UnitGroup:

    def __init__(self, unit_list=None):
        if unit_list is not None:
            self._units = {unit.get_id(): unit for unit in unit_list}
        else:
            self._units = {}

    def add_unit(self, unit):
        self._units[unit.get_id(), unit]

    def remove_unit(self, id):
        self._units.pop(id)

    def get_unit(self, id):
        return self._units[id]

    def get_units(self):
        return list(self._units)


class Weapon:
    pass


class UnitTester(unittest.TestCase):

    def setUp(self):
        self._unit = Unit(1000)

    def test_type(self):
        "Testing setting/getting the type property"
        self._unit.set_type("infantry")
        self.assertEqual(self._unit.get_type(), "infantry")

    def test_specific_property(self):
        "Testing setting/getting a unit-specific property"
        self._unit.set_property('hit_points', 25)
        self.assertEqual(self._unit.get_property('hit_points'), 25)

    def test_non_existent_property(self):
        "Testing getting a non-existent property's value."
        self.assertRaises(KeyError, self._unit.get_property, 'strength')


if __name__ == '__main__':
    unittest.main()
