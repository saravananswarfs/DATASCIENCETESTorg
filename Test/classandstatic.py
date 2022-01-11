class Father:
    __gender="male"
    def __init__(self,name):
        self.name=name
    @classmethod
    def _prin(cls,name):
        print("father can be generated")
        #print(f"the gender is {cls.gender}")
        return cls(name)
    @staticmethod
    def _pri():
        print(f"the gender is gender")
f1=Father._prin("sam")
print(f1.name)
class Child(Father):
    pass

'''class Grandchild(Father):
    def pr(self):
        print(Father._gender)

Child._pri()
c2=Child._prin("saran")
print(c2.name)'''

#print(Father._gender)
'''
gc=Grandchild("ram")
gc.pr()'''