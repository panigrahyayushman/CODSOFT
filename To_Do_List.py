while(True):
    list1=[]
    print("1-To create\n2-Update\n3-Exit")
    
    def list_add():
        n1=int(input("Enter number of data: "))
        for i in range(1,n1+1):
            data=input(f"Enter the data {i}: ")
            list1.append(data)
        print(list1)
   
    def list_update(data):
        n1=input("Enter number of data: ")
        for i in range(1,n1+1):
            data=input(f"Enter the data {i}: ")
            list1.append(data)
        print(list1)
    
    ch=int(input("Enter your choice: "))
    if ch==1:
        list_add()
    elif ch==2:
        list_update()
    elif ch==3:
        break
    else:
        print("Wrong choice....")