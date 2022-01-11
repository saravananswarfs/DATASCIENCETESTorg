gender=input("Please enter the gender : ").strip()
if(gender.lower()=="male"):
    print("please enter the First floor")
elif(gender.upper()=="FEMALE"):
    print("Please visit second floor")
elif(gender.lower()=="others"):
    print("please go the third floor")
elif(gender==""):
    pass
else:
    print("thank you! visit again")
