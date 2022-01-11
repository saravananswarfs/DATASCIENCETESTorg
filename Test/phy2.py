from Test.phy1 import myfunction
if __name__ =="__main__":
    print(f"the source file is executed as {__name__}")
else:
    print(f"imported file name is  {__name__}")
    myfunction()