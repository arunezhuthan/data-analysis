mail=input()
temp=mail.split(".")
print(temp)
temp1=temp[1]
print(temp1)
temp2=temp1.split("@")
print(temp2)
if (int(len(temp2[0]))<=4):
    print("invalid mail:")
print("added the new line")
