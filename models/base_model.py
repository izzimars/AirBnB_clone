#!/usr/bin/python3
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

import uuid
from datetime import datetime
import models


class BaseModel:
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

    def __init__(self, *args, **kwargs):
        """ Initialization method for the base model instances, this
        initializes an id property[id], time created
        property[created_at], and time updated[updated_at].

        return: None.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            for i in kwargs:
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.fromisoformat(kwargs[i])
                    continue
                self.__dict__[i] = kwargs[i]
        else:
            models.storage.new(self)

    def __str__(self):
        """ A mehod that print a repesentation of the instance.

        params: None.
        return type: string.
        return value: returns a string representation of the instance.
        """

        string = "[{}] ({}) {}"
        return string.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ A method that updates the public instance attribute
        updated_at with the current datetime

        params: None.
        return: None.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ A method that returns a dictionary containing all
        keys/values of the instance

        params: None.
        return type: dictionary.
        return value: returns a dictionary containing all keys/values
                      of __dict__ of the instance.
        """

        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
