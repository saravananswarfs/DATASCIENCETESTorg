class Ball:
    shape="Round"
    def __init__(self,name,radius):
        self.name=name
        self.radius=radius
    def prin(self):
        print(f"please start play with {self}")
class Football(Ball):
    def __init__(self,name,brand,radius):
        self.brand=brand
        super().__init__(name,9.78)
fb1=Football(99.0,"Puma",3.14)
print(fb1.name)
fb1.prin()

a=object()
print(a)


