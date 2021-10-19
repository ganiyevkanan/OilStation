"""

1.Guest(her bir sehifede exit olsun)
	1.1 Oil Station
		1.1.1 Benzin Novleri sechilsin
                      AI-92 - 1.0 azn
	                AI-95 - 1.45
                      AI-98 - 1.9
                      Dizel - 0.8
                     1.1.1.1  With liter or money ?(emeliyyat sonda pdf fayla yazilsin)
        1.2 Cafe
		1.2.1 Fast Food sechilsin
                      Hamburger 5.4
                      Free      3.8
                      Cola      1.5
                      Red-bull  4.8
                      sechim haqqi her defe elave oluna biler               
2.Admin

1.1 Username , Password
1.1.1 Welcome Admin Page
      1.Add UserAdmin
      2.Add Petrol
      3.Delete Petrol
      4.Add fast Food
      5.Delete fast food
      4.Exit
#Butun meulumatlar hamisi fayldan gelsin 
#Pdf e check chixsin
YA DICTIONARY ISTIFADE EDIN YA DA CLAS VE OBYEKTLERDEN

"""

#1.Entery admin & guest
#Admin username & password
#Add UserAdmin #Add Petrol #Delete Petrol #Add fast Food #Delete fast food #Exit/
from menu import Menu
from buyPetrol import BuyPetrol
from buyFood import BuyFood
import time
from user import User
from food import Food
from petrol import Petrol
try:
      while True:
            entry=input("Who are you? Admin(a)/Guest(g)\nFor exit (q): ")
            if(entry=="a"):
                  time.sleep(2) 
                  username=input("Enter username: ")
                  password=input("Enter password: ")
                  total=User.getUsers()
                  access=False
                  for i in total:
                        if(i[0]==username and i[1]==password):
                              print("Welcome!")
                              access=True
                              break
                  if(not access):
                        raise Exception("Access denied")
                  while True:
                        print(Menu.showMenuforAdmin())
                        select=input("Enter opeation: ")
                        if(select=="1"):
                              username=input("Enter username: ")
                              password=input("Enter password: ")
                              user=User(username,password)
                              time.sleep(3)
                              print(user.addUser())
                        elif(select=="2"):
                              petrol_name=input("Enter petrol name: ")
                              result=Petrol.checkPetrolName(petrol_name)
                              if(result):
                                    petrol_price=input("Enter petrol price: ")
                                    petrol_capacity=input("Enter petrol capacity: ")
                                    petrol=Petrol(petrol_name,petrol_price,petrol_capacity)
                                    time.sleep(2)
                                    print(petrol.addPetrol())
                                    print()
                                    time.sleep(1)
                                    print(petrol.showPetrol())
                              else:
                                    yesornot=input("We have this petrol. Do you want to update its capacity? \nFor yes(y)\nFor no(n): ")
                                    if(yesornot=="y"):
                                          petrol_capacity=input("Enter capacity: ")
                                          print(Petrol.updateCapacity(petrol_name,petrol_capacity))
                                    elif("n"):
                                          print("OK")

                        elif(select=="3"):
                              print(Petrol.showPetrol())
                              petrol_name=input("Enter petrol name: ")
                              print(Petrol.removeFromFile(petrol_name))
                              print()
                              print()
                              time.sleep(3)
                              print(Petrol.showPetrol())
                        
                        elif(select=="4"):
                              food_id=input("Enter food ID: ")
                              total=Food.readFile()
                              result=True
                              
                              if(result==True):
                                    check=Food.checkFoodID(food_id)
                                    if(check==True):
                                          food_name=input("Enter food name: ")
                                          food_price=input("Enter food price: ")
                                          food_number=input("Enter food number: " )
                                          food=Food(food_id,food_name,food_price,food_number)
                                          print(food.addFood())
                                          print()
                                          print("Loading...")
                                          time.sleep(3)
                                          print(food.showFood())
                                    else:
                                          yesornot=input("We have this food. Do you want to change its count\nFor yes (y)\nFor not (n): ")
                                          food_number=input("Enter food number: " )
                                          if(yesornot=="y"):
                                                print(Food.updateNumber(food_id,food_number))
                                          elif(yesornot=="n"):
                                                print("OK")
                                          else:
                                                print("Valid operation!")
                        elif(select=="5"):
                              print(Food.showFood())
                              UID=input("Enter petrol ID: ")
                              print("Removing...")
                              time.sleep(3)
                              print(Food.removeFromFile(UID))
                              print()
                              print()
                              print(Food.showFood())
                        elif(select=="q"):
                              break
            elif(entry=="g"):
                  time.sleep(2) 
                  print("Welcome!")
                  print()
                  while True:
                        print(Menu.showMenuforUser())
                        sum=0
                        select=input("Enter: \nFor Oil Station(1)\For Cafe(2)\nExit(q): ")
                        if(select=="1"):
                              time.sleep(2)
                              print(Petrol.showPetrolforUser())
                              petrol_name=input("Enter petrol name: ")
                              a_type=input("Enter type (l)/(m):  ")
                              amount=int(input("Enter amount: "))
                              print("Calculating...")
                              time.sleep(2)
                              print(BuyPetrol.sell(petrol_name,amount,a_type))
                        elif(select=="2"):
                              total_monay=0
                              while True:
                                    opp=input("For exit(q):\nFor continue(c): ")
                                    if(opp=="q"):
                                          print("Loading...")
                                          time.sleep(3)
                                          file=BuyFood.isEmpty()
                                          if(file):
                                                print(BuyFood.addtotalMoney(total_monay))
                                                print(BuyFood.getPdf())
                                                print(BuyFood.clearReceipt())
                                          break
                                    elif(opp=="c"):
                                          print(Food.showFoodforUser())
                                          id=input("Enter food id: ")
                                          amount=int(input("Enter food amount: "))
                                          check=(BuyFood.yesAmount(id,amount))
                                          if(check):
                                                print(BuyFood.sell(id,amount))
                                                money=BuyFood.money(id,amount)
                                                total_monay+=money
                                                BuyFood.getReceipt(id,amount)
                                          else:
                                                print("Product is unavaiable")
                                    else:
                                          print("Valid opeartion!")
                        elif(select=="q"):
                              time.sleep(2)
                              break
                        else:
                              print("Valid selection!")
            elif(entry=="q"):
                  time.sleep(2)
                  break
            else:
                  print("Valid Operation!")
except Exception as ex:
      print(ex)