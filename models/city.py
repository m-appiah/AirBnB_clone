#!/usr/bin/python3
""" Defines the City class. """
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines the City class which inherits the BaseModel.

    Args:
        state_id (str): The state id.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
