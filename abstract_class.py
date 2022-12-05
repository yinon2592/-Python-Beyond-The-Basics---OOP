from abc import ABC, abstractmethod

class GetterSetter(ABC):
    @abstractmethod
    def set_val(self, input):
        """Set a value in the instance"""
        return
    @abstractmethod
    def get_val(self):
        """Get and return a value from the instance"""
        return

class A(GetterSetter):
    def __init__(self):
        self.aa = 1
    def set_val(self, input):
        pass

    def get_val(self, input):
        pass
# b = GetterSetter()
a = A()
print(a)
print("a id = {0} and this {1}".format(id(a),"great"))