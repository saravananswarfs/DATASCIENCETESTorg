s=input("Enter the name inn capitalize format : ").strip()
for i in s:
    if i.isupper():
        print(f"capital {i}")
    else:
        continue
        #print(f"small {i}")
else:
    print("No more enteries")


li=[(1,2),(3,4),(4,5)]
for i in li:
    print(li)
for i,y in li:
    print(i)
    print(y)




