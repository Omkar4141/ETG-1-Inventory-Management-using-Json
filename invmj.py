#this module contains functions to working with json data .or working with file presented in json.

import json
record={
    1001:{"Name":"Mango","Quantity":34,"Price":10},
    1002:{"Name":"Banana","Quantity":30,"Price":15},
    1003:{"Name":"coconut","Quantity":25,"Price":30}
}
js=json.dumps(record)#we use it when we require ob in string format
#dump():when python ob have to stored in file
f=open("omkar1.json","w")
f.write(js)
f.close()

fr=open("omkar1.json","r")
r=fr.read()
fr.close()

record=json.loads(r)#to convert json string into python dictonary



while(True):
    print("***Welcome To Fruit Market***")

    print("1:Customer" )
    print("2.Owner")
    print("3.Exit")
    a=int(input("Enter Choice:"))
    if(a==1):
        print("**************")
        print("Avaiable Products:")
        print("1001:Mango and " + "Avaiable Quantity:" +str(record["1001"]["Quantity"]))
        print("1002:Banana and " + "Avaiable Quantity:" +str(record["1002"]["Quantity"]))
        print("1003:Coconut and " + "Avaiable Quantity:" +str(record["1003"]["Quantity"]))
        print("*************")
        k=str(input("Enter Product id:"))
        q=int(input("Enter Quantity:"))
        print("*************")
        if(q>record[k]["Quantity"]):
            print("only"+ str(record[k]["Quantity"]) +"pieces aavaiable...! \n Sorry for Inconvinience")
        else:
            print("...enter details to generate bill...")
            print("**************")
            name=input("Name:")
            mob_no=int(input("Mobile no:"))
            record[k]["Quantity"]=record[k]["Quantity"]-q
            print("***************")
            print("Product ID:",k)
            print("Name:",record[k]["Name"])
            print("Quantity:",q)
            print("Price:",record[k]["Price"])
            print("***************")
            print("Total Amount:",record[k]["Price"]*q)
            print("**************")
    elif(a==2):
        username=input("UserName:")
        Pass=input("Passward:")
        if(username=='Omkar' and Pass=='Omkar@4141'):
            print("Hellow" + username+"...!")
            while(True):
                print("You have Following rites:\n1.update product id\n2.update Quantity\n3.update Price\nPress anything to Exit")
                o=int(input("Enter Choice:"))
                if(o==1):
                    pid=input("Enter product id:")
                    record[pid]=pid
                elif(o==2):
                    pik = input("Enter Product id whose Quantity u have to update:")
                    newq = int(input("New Quantity:"))
                    record[pik]["Quantity"] = newq
                elif(o==3):
                    pii=input("Enter Product id whose price u have to update:")
                    newp=int(input("New Price:"))
                    record[pii]["Price"]=newp
                else:
                    break
        else:
            print("Please Enter Coreect Details")


    else:
        exit()