class MyClass:
    def __enter__(self):
        print ('we have entered "with"')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print ('we are leaving  "with"')
        print(f'error type: {exc_type}')
        print(f'error value: {exc_val}')
        print(f'error traceback: {exc_tb}')
    def sayhi(self):
        print('hi, instance %s'%(id(self)))

with MyClass() as cc:
    cc.sayhi()
    5/0

print('after the "with" block')