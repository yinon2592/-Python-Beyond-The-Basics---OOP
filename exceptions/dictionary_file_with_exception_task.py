import sys
from os.path import isfile

class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()
    def __str__(self):
        return f'key "{self.key}" is not foun. available keys: {", ".join(self.keys)}'

class ConfigDict(dict):
    def __init__(self, filename):
        self._filename = filename
        if not isfile(self._filename):
            try:
                open(self._filename,'w').close()
            except :IOError("arg to ConfigDict must be a valid path")
        with open(self._filename) as fh:
            for line in fh:
                line = line.rstrip()
                key, value = line.split('=', 1)
                dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        dict.__setitem__(self,key,value)
        with open(self._filename, 'w') as fh:
            for key, val in self.items():
                fh.write(f'{key} = {val}\n')
    def __getitem__(self, key):
        if not key in self.keys():
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self,key)

# cc = ConfigDict("dict.txt")
# # open("dict.txt", 'w').close()
# # cc.clear()
# cc['a'] = 1
# cc['b'] = 2
# cc['c'] = 3
# system('cmd /c "type dict.txt"')
