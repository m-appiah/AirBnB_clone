#!/usr/bin/python3
""" Defines the Amenity class. """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines the Amenity class which inherits the BaseModel.

    Args:
        name (str): The name of the amenity.
    """
    name = ""
