def cmplm(x):
    z=list()
    for i in range(len(x)):
        if(x[i]=="1"):
            z.append("0")
        else:
            z.append("1")
    return "".join(z)   
print("Enter message: ")
msg=raw_input()
print("No. of bits of each slice: ")
b=int(raw_input())
n=len(msg)
parts=list()
x=n/b
for i in range(x):
    parts.append(msg[(i*b):(i+1)*b])
print(parts)
rb="0"*b
for i in range(x):
    rb=str(bin(int(rb,2)|int(parts[i],2)))[2:]
msg=msg+rb
print("Transmitted message: "+msg)
parts1=list()
for i in range(x+1):
    parts1.append(msg[(i*b):(i+1)*b])
print(parts1)
rb="0"*b
for i in range(x+1):
    rb=str(bin(int(rb,2)|int(parts1[i],2)))[2:]
print("error checker output: "+cmplm(rb))
