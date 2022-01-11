def myfunc(**para,*para1):
    print(para)
    print(para1)
per1={'name':"susan",'age':40,'exp':12,'location':'chennai','married':'yes'}
per2={'name':"susan",'age':50,'exp':12,'location':'chennai','married':'No'}
print(per1)
myfunc(name='susan',age=20,exp=1,married='yes',1,2,3,4,5)
