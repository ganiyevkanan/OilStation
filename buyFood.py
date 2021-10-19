from os import read
from food import Food
from fpdf import FPDF

class BuyFood():
    def __init__(self,food_id,amount):
        self.setFoodID(food_id)
        self.setAmount(amount)

    def setFoodID(self,food_id):
        self.__food_id=food_id
    def getFoodID(self):
        return self.__food_id
    
    def setAmount(self,amount):
        self.__amount=amount
    def getAmount(self):
        return self.__amount

    @staticmethod
    def sell(food_id,amount):
        total=Food.readFile()
        for t in total:
            if(food_id==t[0]):
                if(amount<=int(t[3])):
                    #money=amount*float(t[2])
                    total_food=int(t[3])-amount
                    t[3]=str(total_food)
                    #print("Money: {} ".format(money))
                    break 
        with open("food.txt","w",encoding="utf-8") as file:
            file.write("")
        for i in total:
            if(i[0]==""):
                continue
            with open("food.txt","a",encoding="utf-8") as file:
                file.write("{id},{name},{price},{count}\n".format(id=i[0],name=i[1],price=i[2],count=i[3]))
        return "---------------------------------------------------------------------"
    def sellProduct():
        print(BuyFood.sell)

    
    def money(food_id,amount):
        total=Food.readFile()
        for t in total:
            if(food_id==t[0]):
                if(amount<=int(t[3])):
                    return (amount*(float(t[2])))
                    
    def getIdforReceipt():
        with open("food_receipt.txt","r",encoding="utf-8") as file:
            receipt=file.readline()
        return str(receipt)
    def getReceipt(id,amount):
        total=Food.getFood()
        for i in total:
            if(i[0]==id):
                with open("receipt.txt","a",encoding="utf-8") as file:
                    r=amount*float(i[2])
                    file.write("\n")
                    file.write(" {} x {} ={} AZN".format(i[1],amount,r))
                    return "------------"
    def getPdf():
        pdf = FPDF()   
      
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        
        
        f = open("receipt.txt", "r")
        
        for x in f:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

        receipt=BuyFood.getIdforReceipt()

        
        pdf.output("cafe_{}.pdf".format(receipt)) 
        with open("food_receipt.txt","w",encoding="utf-8") as file:
            id=int(receipt)+1
            file.write(str(id))
        return "Your receipt"
    
    def clearReceipt():
        with open("receipt.txt","w",encoding="utf-8") as file:
            file.write("")
            return "-------"

    def addtotalMoney(total_money):
        with open("receipt.txt","a",encoding="utf-8") as file:
            file.write("\n")
            file.write("Total money: "+str(total_money))
        return "--------"
    @staticmethod
    def yesAmount(food_id,amount):
        total=Food.readFile()
        check=False
        for t in total:
            if(food_id==t[0] and amount<=int(t[3])):
                check=True
                break
        return check
    def isEmpty():
        with open("receipt.txt","r",encoding="utf-8") as file:
            read=file.read()
            if(read==""):
                return False
            else:
                return True
    

            


            
            
                


