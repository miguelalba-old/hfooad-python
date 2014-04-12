"""
Maria's dogdoor

Author: m1ge7
Date: 2014/04/12
"""


from threading import Timer
import time


class Bark:

    def __init__(self, sound):
        self._sound = sound

    def get_sound(self):
        return self._sound

    def __eq__(self, bark):
        return self._sound.lower() == bark.get_sound().lower()


class BarkRecognizer:

    def __init__(self, door):
        self._door = door

    def recognize(self, bark):
        print("   BarkRecognizer: Heard a '" + bark.get_sound() + "'")
        for allowed_bark  in self._door.get_allowed_barks():
            if allowed_bark == bark:
                self._door.open()
                return
        print("This dog is not allowed.")


class DogDoor:

    def __init__(self):
        self._allowed_barks = []
        self._open = False

    def add_allowed_bark(self, bark):
        self._allowed_barks.append(bark)

    def get_allowed_barks(self):
        return self._allowed_barks

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
    door.add_allowed_bark(Bark("rowlf"))
    door.add_allowed_bark(Bark("rooowlf"))
    door.add_allowed_bark(Bark("rawlf"))
    door.add_allowed_bark(Bark("woof"))
    recognizer = BarkRecognizer(door)
    remote = Remote(door)

    # Simulate the hardware hearing a bark
    print("Bruce starts barking.")
    recognizer.recognize(Bark("Rowlf"))

    print("\nBruce has gone outside...")

    time.sleep(10)

    print("\nBruce all done...")
    print("...but he's stuck outside!")

    # Simulate the hardware hearing a bark (not Bruce!)
    small_dog_bark = Bark("yip")
    print("A small dog starts barking.")
    recognizer.recognize(small_dog_bark)

    time.sleep(5)

    # Simulate the hardware hearing a bark again
    print("\nBruce starts barking.")
    recognizer.recognize(Bark("Rowlf"))

    print("\nBruce's back inside...")
