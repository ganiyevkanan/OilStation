from petrol import Petrol
from fpdf import FPDF
from datetime import date
import random
#user buy petrol
class BuyPetrol():
    def __init__(self,petrol_name,amount):
        self.setPetrolName(petrol_name)
        self.setAmount(amount)

    def setPetrolName(self,petrol_name):
        self.__petrol_name=petrol_name
    def getPetrolName(self):
        return self.__petrol_name
    
    def setAmount(self,amount):
        self.__amount=amount
    def getAmount(self):
        return self.__amount
    @staticmethod
    #selling function
    def sell(petrol_name,amount,a_type):
        total=Petrol.readFile()
        for t in total:
            if(a_type=="l"):
                
                if(petrol_name==t[0]):
                    if(amount<=float(t[2])):
                        money=amount*float(t[1])
                        total_capacity=float(t[2])-amount
                        t[2]=str(total_capacity)
                        print(BuyPetrol.getReceipt(petrol_name,amount,money))
                        break
                    else:
                        print("Petrol is unavaiable")
                        break
            elif(a_type=="m"):
                if(petrol_name==t[0]):
                    litre=amount/float(t[1])
                    if(litre<=float(t[2])):
                        total_capacity=float(t[2])-litre
                        t[2]=str(total_capacity)
                       # print("Litre: {}".format(litre))
                        print(BuyPetrol.getReceipt(petrol_name,litre,amount))
                        break
                    else:
                        print("Petrol is unavaiable")
                        break

        with open("petrol.txt","w",encoding="utf-8") as file:
            file.write("")
        for i in total:
            if(i[0]==""):
                continue

            with open("petrol.txt","a",encoding="utf-8") as file:
                file.write("{name},{price},{capacity}\n".format(name=i[0],price=i[1],capacity=i[2]))
        return "-----------------------------------"
    def getReceipt(petrol_name,litre,money):
        receipt=BuyPetrol.getIdforReceipt()
        pdf = FPDF()
        pdf.add_page()
        
        pdf.set_font("Arial", size = 15)
        today=date.today()
        todayis="{}/ {}/ {}".format(today.year,today.month,today.day)
        pdf.cell(300, 7, txt = todayis,
                ln = 3, align = 'C')
        pdf.cell(200, 15, txt = "KANAN PETROL", 
                ln = 3, align = 'C')
        text1="Petrol: {}".format(petrol_name)
        pdf.cell(70, 7, txt = text1,
                ln = 5, align = 'C')
        text2="Litre: {}".format(litre)
        pdf.cell(70, 7, txt = text2,
                ln = 6, align = 'C')
        petrol=Petrol.getPetrol()
        price=0
        for i in petrol:
            if(i[0]==petrol_name):
                price=float(i[1])
                break
        text3="Money: {}*{} = {} AZN".format(price,litre,money)
        pdf.cell(70, 7, txt = text3,
                ln = 7, align = 'C')
        pdf.output("petrol_{}.pdf".format(receipt)) 
        with open("petrol_receipt.txt","w",encoding="utf-8") as file:
            id=int(receipt)+1
            file.write(str(id))
        return "Your receipt"  
    def getIdforReceipt():
        with open("petrol_receipt.txt","r",encoding="utf-8") as file:
            receipt=file.readline()
        return str(receipt)

                

    
