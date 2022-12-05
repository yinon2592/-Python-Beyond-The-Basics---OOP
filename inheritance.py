class Animal :
    def __init__(self,name="None"):
        print("Animal constrctor")
        self.name = name

class Dog(Animal):
    def __init__(self,name,breed):
        super(Dog,self).__init__(name)
        print("Dog constrctor")
        self.breed = breed
a = Animal()
print("\n")
b = Dog("rocky","rotwiler")
class Instance :
    count = 0
    def __init__(self, val):
        self.val = self.filter_int(val)
        Instance.count += 1

    @staticmethod
    def filter_int(val):
        if not isinstance(val, int):
            return 0
        else:
            return val

    @classmethod
    def get_count(cls):
        return cls.count

a = Instance(5)
b = Instance(13)
c = Instance("hello")
print (a.val) ; print (b.val) ; print (c.val)
print (Instance.get_count())
print (Instance.filter_int("a"))

