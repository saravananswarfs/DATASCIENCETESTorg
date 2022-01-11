from abc import ABC,abstractmethod

class P(ABC):
    nam="saravanan"
    def __init__(self):
        self.ab="sad"
        self.cd="mas"
    @abstractmethod
    def play(self):
        pass
    @staticmethod
    def stop():
        print("the video is stopped")
    @classmethod
    def prin(cls):
        print(cls.nam)

class C(P):
    def play(self):
        print("The song is played")

c1=C()
print(c1)
c1.play()
print(c1.ab)
print(c1.cd)
c1.stop()
c1.prin()