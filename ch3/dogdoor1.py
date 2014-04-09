""" Dog door with barks recognizer

Author: m1ge7
Date: 2014/04/09
"""

import time
from threading import Timer


class DogDoor:
    
    def __init__(self):
        self._open = False

    def open(self):
        print("The dog door opens")
        self._open = True

    def close(self):
        print("The dog door closes")
        self._open = False

    def is_open(self):
        return self._open


class Remote:

    def __init__(self, door):
        self._door = door

    def press_button(self):
        print("Pressing the remote control button...")
        if self._door.is_open():
            self._door.close()
        else:
            self._door.open()
            timer = Timer(5, lambda door: door.close(), [self._door])
            timer.start()


class BarkRecognizer:

    def __init__(self, door):
        self._door = door

    def recognize(self, bark):
        print("   BarkRecognizer: Heard a '" + bark + "'")
        self._door.open()


if __name__ == '__main__':
    door = DogDoor()
    recognizer = BarkRecognizer(door)
    remote = Remote(door)

    # Simulate the hardware hearing a bark
    print("Fido barks to go outside...")
    recognizer.recognize("Woof")

    print("\nFido has gone outside...")
    print("\nFido's all done...")

    time.sleep(10)

    print("...but he's stuck outside!")

    print("\nFido starts barking...")
    recognizer.recognize("Woof")

    print("\nFido's back inside...")
