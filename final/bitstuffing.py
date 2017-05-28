print("Enter Bit Sequence: \n")
s=raw_input()
flag=0
x=list()
for i in range(len(s)):
    x.append(s[i])
    if(s[i]=="1"):
        flag=flag+1
    else:
        flag=0
    if(flag==3):
        x.append("0")
        flag=0
y="".join(x)
print("message sent: "+y)
z=list()
i=0
while(i<len(y)):
    z.append(y[i])
    if(y[i]=="1"):
        flag=flag+1
    else:
        flag=0
    if(flag==3):
        if(y[i+1]=="0"):
            i=i+1
            flag=0
        else:
            flag=2
    i=i+1
w="".join(z)
print("message recieved:"+w)
