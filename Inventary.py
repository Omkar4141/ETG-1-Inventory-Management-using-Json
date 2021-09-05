import json
record={
    1001:{"Name":"Redmi 9 power","RAM":"6GB","Storage":"128GB","Battery":"6000mAH","Quantity":5,"Price":13999},
    1002:{"Name":"Redmi 10 prime","RAM":"4GB","Storage":"64GB","Battery":"5000mAH","Quantity":10,"Price":12999},
    1003:{"Name":"Redmi note 7","RAM":"4GB","Storage":"64GB","Battery":"4000mAH","Quantity":13,"Price":11999},
    1004:{"Name":"Redmi 9A","RAM":"2GB","Storage":"32GB","Battery":"3000mAH","Quantity":20,"Price":7000},
    1005:{"Name":"Redmi note 9 pro","RAM":"6GB","Storage":"128GB","Battery":"5000mAH","Quantity":22,"Price":17000},
    1006:{"Name":"Redmi Lite","RAM":"3GB","Storage":"42GB","Battery":"3500mAH","Quantity":25,"Price":10000},
    1007:{"Name":"Redmi 7","RAM":"6GB","Storage":"42GB","Battery":"4000mAH","Quantity":30,"Price":12100},
    1008:{"Name":"Redmi 6","RAM":"4GB","Storage":"64GB","Battery":"6000mAH","Quantity":30,"Price":20000},
    1009:{"Name":"Redmi 5","RAM":"3GB","Storage":"32GB","Battery":"2000mAH","Quantity":30,"Price":8000},
    1010:{"Name":"Redmi 4u","RAM":"4GB","Storage":"64GB","Battery":"6000mAH","Quantity":30,"Price":6000}
}
js=json.dumps(record)

f=open("omkar11.json","w")
f.write(js)
f.close()

fr=open("omkar11.json","r")
r=fr.read()
fr.close()

record=json.loads(r)
print("*****Welcome To Redmi Mobile Store ,Baramati *****")
while(True):
    print("1.Customer")
    print("2.System Administrater")
    print("3.Exit")
    print("*****************************")
    ch=int(input("Enter Choice:"))
    if(ch==1):
        while(True):
            print("******************************")
            print("1.Avaiable Products")
            print("2.Get Product Details")
            print("3.Purchase Product")
            print("Enter any key Exit")
            print("******************************")
            ch1=int(input("Enter Choice:"))
            if(ch1==1):
                print("These are the avaiable products:")
                print("**********************************")
                for i in range(1001, 1011):
                    print(str(i) + ":" + str(record[str(i)]["Name"]))
            elif(ch1==2):
                id=input("Enter Product Id:")
                print("________________________")
                print("Product Details:")
                print("________________________")
                print("Product ID:" + str(id))
                print("Name:" + str(record[id]["Name"]))
                print("RAM:" + str(record[id]["RAM"]))
                print("Storage:" + str(record[id]["Storage"]))
                print("Battery:" + str(record[id]["Battery"]))
                print("Quantity:" + str(record[id]["Quantity"]))
                print("Price:" + str(record[id]["Price"]))
                print("_______________________________")

            elif(ch1==3):
                print("Enter Details to Generate Bill:")
                print("_______________________________")
                nm=input("Enter Name:")
                mn=int(input("Enter mobile No:"))
                id2=input("Enter Product Id:")
                q = int(input("Enter Quantity:"))
                if (q > record[id2]["Quantity"]):
                    print("only" + str(record[id2]["Quantity"]))
                else:
                    print("_______________________________")
                    print("Name:" + str(record[id2]["Name"]))
                    print("RAM:" + str(record[id2]["RAM"]))
                    print("Storage:" + str(record[id2]["Storage"]))
                    print("Battery:" + str(record[id2]["Battery"]))
                    print("Quantity:" + str(q))
                    record[id2]["Quantity"] = record[id2]["Quantity"] - q
                    print("Price:" + str(record[id2]["Price"]))
                    print("_______________________________")
                    print("Amount:", q * record[id]["Price"])
                    print("______________________________")

            else:
                break
    elif(ch==2):
        user=input("Enter Username:")
        Pass=input("Enter Passward:")
        if(user=='Omkar' and Pass=='Omkar@4141'):
            print("Welcome" + user +"...!")
            while(True):
                print("---------------------")
                print("1.Update Product Quantity")
                print("2.update product price")
                print("Enter any to exit")
                ch3=int(input("Enter Choice:"))
                if(ch3==1):
                    id3=input("Enter id whose quantity u have to update:")
                    nq = int(input("Enter Quantity:"))
                    record[id3]["Quantity"] = nq

                elif(ch3==2):
                    id4 = input("Enter id whose Price u have to update:")
                    np = int(input("Enter new Price:"))
                    record[id4]["Price"] = np

                else:
                    break


        else:
            print("Wrong details")
    else:
        exit()