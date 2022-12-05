import sys
from os.path import isfile
from os import system

class ConfigDict(dict):
    def __init__(self, filename):
        self._filename = filename
        if isfile(self._filename):
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

cc = ConfigDict("dict.txt")
# open("dict.txt", 'w').close()
# cc.clear()
cc['a'] = 1
cc['b'] = 2
cc['c'] = 3
system('cmd /c "type dict.txt"')
