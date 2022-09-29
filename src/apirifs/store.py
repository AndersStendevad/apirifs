""" Store class """

import json
import dbm
import atexit

from pathlib import Path
from os.path import join

class Store:
    """ Store class """
   
    def __init__(self, db_name: str, db_location: Path = join(Path.home(),"db")):
        """ Initialize the store 

        Parameters:
        -----------
        db_name: str
            The name of the database

        db_location: Path
            The location of the database
        """
        self.filename = join(db_location, db_name+".db")
        self.db = dbm.open(self.filename, 'c')
        atexit.register(self.db.close)

    def __getitem__(self, key: str):
        """ Get an item from the store """
        return json.loads(self.db[key].decode('utf-8'))

    def __setitem__(self, key: str, value: dict):
        """ Set an item from the store """
        self.db[key] = json.dumps(value).encode('utf-8')

    def __delitem__(self, key: str):
        """ Delete an item from the store """
        del self.db[key]

    def __iter__(self):
        """ Iterate over items from the store """
        return iter(self.db)

    def __len__(self):
        """ Return the number of items in the store """
        return len(self.db)

    def __contains__(self, key: str):
        """ Check if the store contains a key """
        return key in self.db

    def keys(self):
        """ Return the keys of the store """
        return self.db.keys()

    def values(self):
        """ Return the values of the store """
        return (json.loads(value.decode('utf-8')) for value in self.db.values())

    def items(self):
        """ Return the items of the store """
        return ((key, json.loads(value.decode('utf-8'))) for key, value in self.db.items())

    def get(self, key: str, default=None):
        """ Get an item from the store """
        try:
            return self[key]
        except KeyError:
            return default

    def insert(self, key: str, value: dict):
        """ Insert an item into the store """
        self[key] = value

    def __repr__(self):
        """ Return the representation of the store """
        return 'Store({})'.format(self.filename)
   
