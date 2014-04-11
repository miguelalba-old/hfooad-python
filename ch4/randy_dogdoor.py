"""
Randy's dogdoor

Author: m1ge7
Date: 2014/04/11
"""


from threading import Timer
import time


class BarkRecognizer:

    def __init__(self, door):
        self._door = door

    def recognize(self, bark):
        print("   BarkRecognizer: Heard a '" +  bark + "'")
        if self._door.get_allowed_bark() == bark:
            self._door.open()
        else:
            print("This dog is not allowed.")


class DogDoor:

    def __init__(self):
        self._open = False
        self._allowed_bark = None

    def set_allowed_bark(self, bark):
        self._allowed_bark = bark

    def get_allowed_bark(self):
        return self._allowed_bark

    def open(self):
        print("The dog door opens.")
        self._open = True
        timer = Timer(5, lambda door: door.close(), [self])
        timer.start()

    def close(self):
        print("The dog door closes.")
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


if __name__ == '__main__':
    door = DogDoor()
    door.set_allowed_bark("Rowlf")
    recognizer = BarkRecognizer(door)
    remote = Remote(door)

    # Simulate the hardware hearing a bark
    print("Bruce starts barking.")
    recognizer.recognize("Rowlf")

    print("\nBruce has gone outside...")

    time.sleep(10)

    print("\nBruce all done...")
    print("...but he's stuck outside!")

    # Simulate the hardware hearing a bark (not Bruce!)
    print("A small dog starts barking.")
    recognizer.recognize("Yip")

    time.sleep(5)

    # Simulate the hardware hearing a bark again
    print("\nBruce starts barking.")
    recognizer.recognize("Rowlf")

    print("\nBruce's back inside...")
