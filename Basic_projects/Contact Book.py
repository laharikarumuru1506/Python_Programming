#creating a list of friends information in a book
mybook={}
#for adding the information
def add_info():
    #enter the information of your friend
    frd_nm=input("enter the name: ")
    ph_no = int(input("enter the phone no: "))
    address = input("enter the location: ")
    mybook[frd_nm]={"name":frd_nm,"phno":ph_no,"location":address}
#for updation of the information
def update_info():
    frd_nm = input("enter the name that to be updated: ")
    print("1.updating phno\n2.updating address")
    s=int(input("enter the choice for updation"))
    if s==1:
        ph_no = int(input("enter the phone no: "))
        mybook.update({frd_nm: {"phno":ph_no}})
    else:
        address = input("enter the location: ")
        mybook.update({frd_nm: {"location":address}})
#for deleting the information
def delete_info():
    frd_nm = input("enter the name that to be deleted: ")
    mybook.pop(frd_nm)
#for searching the information
def search_info():
    frd_nm = input("enter the name that to be searched: ")
    if frd_nm in mybook:
        print("It's found!!!!!")
    else:
        print("It's not found!!!!!")
#for displaying the information
def display_info():
    for i,j in mybook.items():
        print(i,j)
while True:
    print("1.add the info\n2.update the info\n3.delete the info\n4.search the info\n5.display the info")
    x=int(input("enter the choice: "))
    if x==1:
        add_info()
    elif x==2:
        update_info()
    elif x==3:
        delete_info()
    elif x==4:
        search_info()
    elif x==5:
        display_info()
    else:
        print("inalid choie....exit")
        break
