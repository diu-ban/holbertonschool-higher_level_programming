#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is student: {}".format(self.is_student))
    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (pickle.PicklingError, IOError) as e:
            print(f"Error during serialization: {e}")
    @classmethod 
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"Error during deserialization: {e}")
            return None
        
