#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        self.set_name(name)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            self._name = None
            print("Name must be string between 1 and 25 characters.")
    name = property(get_name, set_name)
    
    def _init_(self, breed=""):
         self.set_breed(breed)
    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            self._breed = None
            print(f"Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)