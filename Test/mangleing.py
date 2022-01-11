class Test:
    def __init__(self):
        self.foo=11
        self._bar=12
        self.__baz=10
    def __index__(self):
        return 5

    def __len__(self):
        return len
    def __del__(self):
        print("object deleted")
    def __pri(self):
        print("hi sam")
t=Test()
print(t._bar)
print(dir(t))
t._Test__pri()

print(t._Test__baz)
print(t._)
del t