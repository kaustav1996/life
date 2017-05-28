import random
def crc(msg, div, code):
    msg = msg + code
    msg = list(msg)
    div = list(div)
    for i in range(len(msg)-len(code)):
        if msg[i] == '1':
            for j in range(len(div)):
                msg[i+j] = str((int(msg[i+j])+int(div[j]))%2)
    return ''.join(msg[-len(code):])
print("Enter Message: \n")
msg=raw_input()
print("Enter Divisor: \n")
div=raw_input()
v=len(div)
code=crc(msg,div,"0"*(v-1))
print("OUTPUT: "+msg+code)
o=random.randint(0,20)
print(o)
if(o<=10):
    p=random.randint(0,len(msg))
    print(p)
    if(msg[p]=="1"):
        msg=list(msg)
        msg[p]="0"
        msg="".join(msg)
    else:
        msg=list(msg)
        msg[p]="1"
        msg="".join(msg)
    

print("Recieved Perfectly? Ans:- "+str((crc(msg,div,code)=="0"*(v-1))))
          
