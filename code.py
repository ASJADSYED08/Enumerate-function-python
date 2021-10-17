l1=["asjad","ansar","ali","imran","ansar","ali","ansar","ali"]
i=1
for item in l1:
    if i%2!=0:
        print(item)
    i+=1
#enumerate function
for index, item in enumerate(l1):
    if index%2==0:
        print(f"he is {item}")