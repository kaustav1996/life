print("Enter IP address in dotted decimal format")
while(1):
        ip=map(int,raw_input().strip().split("."))
        if(len(ip)!=4):
                print("Invalid IP")
                break
        for i in range(len(ip)):
                if(ip[i]>255 and ip[i]<0):
                        print("Invalid IP")
                        break
        if(ip[0]>=0 and ip[0]<=127):
                print("Class A")
        elif(ip[0]>127 and ip[0]<=191):
                print("Class B")
        elif(ip[0]>=192 and ip[0]<=223):
                print("Class C")
        elif(ip[0]>=224 and ip[0]<=239):
                print("Class D")
        elif(ip[0]>=240 and ip[0]<=255):
                print("Class E")
        else:
                print("Invalid Ip address")
