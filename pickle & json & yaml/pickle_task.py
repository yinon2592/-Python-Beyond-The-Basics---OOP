import os.path
import pickle
import sys
from os.path import system, isfile

class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()
    def __str__(self):
        return f'key "{self.key}" is not foun. available keys: {", ".join(self.keys)}'

class ConfigPickleDict(dict):
    config_directory = 'home/.../configs/'
    def __init__(self, picklename):
        self._filename = os.path.join(ConfigPickleDict.config_directory, picklename+'.pickle')
        if not isfile(self._filename):
            with open(self._filename, 'wb') as fh:
                pickle.dump({}, fh) # writing empty dict to prevent problem later on (we need at least empty dict)
        with open(self._filename) as fh:
            pkl = pickle.load(fh)
            self.update(pkl) # update our dict with the dict coming from pkl

    def __getitem__(self, key):
        if not key in self.keys():
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self,key)

    def __setitem__(self, key, value):
        dict.__setitem__(self,key,value)
        with open(self._filename, 'w') as fh:
            pickle.dump(self, fh)


cc = ConfigDict("dict.txt")