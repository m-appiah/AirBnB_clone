#!/usr/bin/python3
"""Package initialization"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
