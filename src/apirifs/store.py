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

    def __getitem__(self, key: str):
        """ Get an item from the store """
        with dbm.open(self.filename, 'r') as db:
            return json.loads(db[str(key)])

    def __setitem__(self, key: str, value: dict):
        """ Set an item from the store """
        with dbm.open(self.filename, 'c') as db:
            db[str(key)] = json.dumps(value, separators=(',', ':'))

    def __delitem__(self, key: str):
        """ Delete an item from the store """
        with dbm.open(self.filename, 'c') as db:
            del db[str(key)]

    def __iter__(self):
        """ Iterate over items from the store """
        with dbm.open(self.filename, 'r') as db:
            return iter(db)

    def __len__(self):
        """ Return the number of items in the store """
        with dbm.open(self.filename, 'r') as db:
            return len(db)

    def __contains__(self, key: str):
        """ Check if the store contains a key """
        with dbm.open(self.filename, 'r') as db:
            return str(key) in db

    def keys(self):
        """ Return the keys of the store """
        with dbm.open(self.filename, 'r') as db:
            return (str(key) for key in db.keys())

    def values(self):
        """ Return the values of the store """
        return (json.loads(self[key]) for key in self.keys())

    def items(self):
        """ Return the items of the store """
        return ((key, json.loads(self[key])) for key in self.keys())

    def get(self, key: str, default=None):
        """ Get an item from the store """
        try:
            return self[str(key)]
        except KeyError:
            return default

    def insert(self, key: str, value: dict):
        """ Insert an item into the store """
        self[str(key)] = json.dumps(value)

    def __repr__(self):
        """ Return the representation of the store """
        return 'Store({})'.format(self.filename)
   
