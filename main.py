# Health Management System
# 3 clients - Harry, Rohan and Hammad
# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

import datetime
harrF = open("harryF.txt", "r+")
harrEx = open("harryEx.txt", "r+")
hamF = open("hammadF.txt", "r+")
hamEx = open("hammEx.txt", "r+")
rohF = open("rohanF.txt", "r+")
rohEx = open("rohanEx.txt", "r+")

userName = input("Enter your name : ")


if (userName == 'harry'):
    print (f"Hello {userName} what you want press 1 for food detaile 2 for exercise detail")
    det = int(input())
    if (det == 1):
        print (f"Hello {userName} what you want press 1 for food retrive 2 for food log")
        det2= int(input())
        if(det2==1):
            # harrF.seek(0)
            data = harrF.read(100)
            if len(data) == 0 :
                print("You have no data stored , befor you retrive Please add food details")
                harrF.write(input() + f" {datetime.datetime.now()}")
              
            else:
                print("Your food detaile : ",  data)
                # print(f"Your food detaile {harrf.readline()}")
        else:
            harrF.seek(0)
            data = harrF.read(100)
            if len(data) > 0 :
                harrF.write("\n")
            harrF.write(input() + f" {datetime.datetime.now()}")
    else:
        print (f"Hello {userName} what you want press 1 for Exercise retrive 2 for Exercise log")
        det3= int(input())
        if(det3==1):
            harrEx.seek(0)
            data = harrEx.read(100)
            if len(data) == 0 :
                print("You have no data stored , befor you retrive Please add Exercise details")
                harrEx.write(input() + f" {datetime.datetime.now()}")
            else:
                print("Your Exercise detaile : ",data)
        else:
            harrEx.seek(0)
            data = harrEx.read(100)
            if len(data) > 0 :
                harrEx.write("\n")
            harrEx.write(input() + f" {datetime.datetime.now()}")

elif (userName == 'hammad'):
    print (f"Hello {userName} what you want press 1 for food detaile 2 for exercise detail")
    det = int(input())
    if (det == 1):
        print (f"Hello {userName} what you want press 1 for food retrive 2 for food log")
        det2= int(input())
        if(det2==1):
            hamF.seek(0)
            data = hamF.read(100)
            if len(data) == 0 :
                print(print("You have no data stored , befor you retrive Please add food details"))
                hamF.write(input() + f" {datetime.datetime.now()}")
            else:
                print("Your food detaile : ",data)
        else:
            hamF.seek(0)
            data = hamF.read(100)
            if len(data) > 0 :
                hamF.write("\n")
            hamF.write(input() + f" {datetime.datetime.now()}")
    else:
        print (f"Hello {userName} what you want press 1 for Exercise retrive 2 for Exercise log")
        det3= int(input())
        if(det3==1):
            hamEx.seek(0)
            data = hamEx.read(100)
            if len(data) == 0 :
                print("You have no data stored , Please add EXercise details")
                hamEx.write(input() + f" {datetime.datetime.now()}")
            else:
                print("Your Exercise detaile : ",data)
        else:
            hamEx.seek(0)
            data = hamEx.read(100)
            if len(data) > 0 :
                harrEx.write("\n")
            hamEx.write(input() + f" {datetime.datetime.now()}")
            
else:
    print (f"Hello {userName} what you want press 1 for food detaile 2 for exercise detail")
    det = int(input())
    if (det == 1):
        print (f"Hello {userName} what you want press 1 for food retrive 2 for food log")
        det2= int(input())
        if(det2==1):
            rohF.seek(0)
            data = rohF.read(100)
            if len(data) == 0 :
                print("You have no data stored ,Please add food details")
                rohF.write(input() + f" {datetime.datetime.now()}")
                
            else:
                print("Your food detaile :",data)
        else:
            rohF.seek(0)
            data = rohF.read(100)
            if len(data) > 0 :
                rohF.write("\n")
            rohF.write(input() + f" {datetime.datetime.now()}")
    else:
        print (f"Hello {userName} what you want press 1 for Exercise retrive 2 for Exercise log")
        det3= int(input())
        if(det3==1):
            rohEx.seek(0)
            data = rohEx.read(100)
            if len(data) == 0 :
                print("You have no data stored , Please add EXercise details")
                rohEx.write(input() + f" {datetime.datetime.now()}")
            else:
                print("Your Exercise detaile : ",data)
        else:
            rohEx.seek(0)
            data = rohEx.read(100)
            if len(data) > 0 :
                rohEx.write("\n")
            rohEx.write(input() + f" {datetime.datetime.now()}")