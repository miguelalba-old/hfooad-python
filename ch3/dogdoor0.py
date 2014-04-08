""" Dog door - initial version at chapter 3

Author: m1ge7
Date: 2014/04/08
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


if __name__ == '__main__':
    door = DogDoor()
    remote = Remote(door)

    print("Fido barks to go outside...")
    remote.press_button()

    print("\nFido has gone outside...")
    print("\nFido's all done...")

    time.sleep(1)

    print("...but he's stuck outside!")

    print("\nFido starts barking...")
    print("...so Gina grabs the remote control.")
    remote.press_button()

    print("\nFido's back inside...")
