print("\n")
print("1:insert data")
print("2:display data")
ch = int(input("enter your choice:"))
if ch == 1:
    choice="Y"
    while choice=="Y":
        techid=input("Enter technology name:")
        techdes=input("Enter technology description:")
        duration=input("Enter technology duration:")
        str=techid+","+techdes+","+duration+"\n"
        fh = open("technolgoy.txt","a+")
        fh.write(str)
        choice=input("Do you want to insert more data: Y/N")
        fh.close()
elif ch == 2:
    fh1=open("technolgoy.txt","r")
    x=fh1.read()
    print(x)
    fh1.close()     
else:
    print("wrong choice")

file = open("technology.txt","r")
while(file.readline()):
    print("" ,);
    data=list(file.readline().split(","))
    print("Description:{}".format(data[1]))
file.close()
