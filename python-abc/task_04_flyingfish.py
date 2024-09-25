#!/usr/bin/python3
"""
module flyingfish
"""


class Fish:
    def swim(self):
        """
        method swim
        """
        print("The fish is swimming")

    def habitat(self):
        """
        method habitat
        """
        print("The fish lives in water")


class Bird:
    def fly(self):
        """
        method fly
        """
        print("The bird is flying")

    def habitat(self):
        """
        method habitat
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        """
        method fly
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        method swim
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        method habitat
        """
        print("The flying fish lives both in water and the sky!")
