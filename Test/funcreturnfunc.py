def a():
    print("function a is executed")
def b():
    print("function b is executed")
    return a
first=b
print(first)
rel=first()
print(rel)
rel()