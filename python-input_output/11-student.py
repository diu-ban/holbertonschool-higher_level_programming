#!/usr/bin/python3

"""
Module that defines the Student class for JSON serialization.
"""

class Student:
    """
    Represents a student with first name, last name, and age.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance
        for easy JSON serialization.

        Args:
            attrs (list, optional): A list of attribute names to include.
                                    If None or not a list of strings, returns all attributes.

        Returns:
            dict: A dictionary containing all the student's attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json(dict): A dictionary where each key is the name of a public attribute 
                     and the corresponding value is the new value for that attribute.
        """
        for attr in json: 
            setattr(self, attr, json[attr])
