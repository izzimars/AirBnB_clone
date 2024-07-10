#!/bin/python3
"""
base_geometry Module
====================

This module defines the MyList class, which inherits from
the built-in list class.

BaseGeometry:
    MyList: A subclass of list with additional functionality.

Public Function:
    None.

"""


import json
from models.base_model import BaseModel


class FileStorage:
    """
    BaseGeometry Class

    A base class hat defines all common attributes/methods for
    other model.

    Public Methods:
        save: updates the public instance attribute updated_at with
              the current datetime
        to_dict: returns a dictionary containing all keys/values
                 of __dict__ of the instanc

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ A method that returns a dictionary of saved object instances
        in dictionary form.

        params: None.
        return type: None.
        return value: None.
        """
        return FileStorage.__objects

    def new(self, obj):
        """ A method that sets an internal dictionary variable with the
        dictionary instance of obj with the key as  <obj class name>.id.

        params: Object.
        return: None.
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """ A method that serializes the internal dictionary variable
        into a JSON object and save it in a file.

        params: None.
        return: None.
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """ A method that serializes the JSON file into a python
        dictionary and assign it to its internal variable.

        params: None.
        return: None.
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
