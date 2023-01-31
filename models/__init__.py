#!/usr/bin/python3
# creating a unique instance of application


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
