#!/usr/bin/python3
"""Defines the FileStorage class."""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json
from os.path import exists


class FileStorage:
    """
    Handles the serialization and deserialization of
    instances to and from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary containing all stored instances."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new instance to the storage.

        Args:
            obj: The instance to be added to the storage.

        Notes:
            The instance is stored in the format "<class_name>.<id>"
            as the key in the __objects dictionary.
        """
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serializes stored instances to the JSON file."""
        object_dict = {
            key: obj.to_dict() for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to restore stored instances,
        if the file exists.

        If the file does not exist, this method does nothing.
        """
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                object_dict = json.load(file)
                for serialized_obj in object_dict.values():
                    class_name = serialized_obj["__class__"]
                    del serialized_obj["__class__"]
                    self.new(eval(class_name)(**serialized_obj))
