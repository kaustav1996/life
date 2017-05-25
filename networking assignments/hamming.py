#HAMMING CODE GENERATOR of any length by KAUSTAV BANERJEE [KGEC]
print("Enter a message: ")
message=list(raw_input())
parity_pos=list()
bit=0
x=1
while(x<=len(message)):
    parity_pos.append(x)
    bit=bit+1
    x=2**bit
arr=list()
temp=message[::-1]
for i in range(len(message)+len(parity_pos)):
    if(i+1 in parity_pos):
        arr.append("000")
    else:
        arr.append(temp.pop())
print(arr)
for i in range(len(arr)):
    if(arr[i]=="000"):
        skip_check=i+1
        count=0
        j=i
        while(j<len(arr)):
            temp=j
            while(j<temp+skip_check and j<len(arr)):
                if(arr[j]=="1"):
                    count=count+1
                j=j+1
            j=j+skip_check
        if(count%2==0):
            arr[i]="0"
        else:
            arr[i]="1"
print("transmitted message: "+''.join(arr))
print("_"*25)
print("Enter where you want to insert an error, choose a number from 1 to "+str(len(arr))+" (length of transmitted bit)")
e=int(raw_input())
if(arr[e-1]=="0"):
    arr[e-1]="1"
else:
    arr[e-1]="0"
print("message with error: "+''.join(arr))
wrongpos=0
for i in range(len(arr)):
    if(i+1 in parity_pos):
        skip_check=i+1
        count=0
        j=i
        while(j<len(arr)):
            temp=j
            while(j<temp+skip_check and j<len(arr)):
                if(arr[j]=="1" and j!=i):
                    count=count+1
                j=j+1
            j=j+skip_check
        if(count%2==0):
            if(arr[i]!="0"):
                wrongpos=wrongpos+i+1
        else:
            if(arr[i]!="1"):
                wrongpos=wrongpos+i+1
print("Bad BIt Position : "+str(wrongpos))
