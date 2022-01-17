class UserEx(Exception):
    def __init__(self,v="Value greater than 99",d=0):
        self.value=v
        self.data=d
    def __str__(self):
        return(self.value)

