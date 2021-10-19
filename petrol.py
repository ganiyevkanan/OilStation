


class Petrol:
    
            
      
    def __init__(self,petrol_name,petrol_price,petrol_capacity):
        self.setPetrolName(petrol_name)
        self.setPetrolPrice(petrol_price)
        self.setPetrolCapacity(petrol_capacity)


    def setPetrolName(self,petrol_name):
        self.__petrol_name=petrol_name
    def getPetrolName(self):
        return self.__petrol_name
    
    def setPetrolCapacity(self,petrol_capacity):
        self.__petrol_capacity=petrol_capacity
    def getPetrolCapacity(self):
        return self.__petrol_capacity
      

    def setPetrolPrice(self,petrol_price):
        self.__petrol_price=petrol_price
    def getPetrolPrice(self):
        return self.__petrol_price
    #this function update petrol capacity
    @staticmethod
    def updateCapacity(petrol_name,petrol_capacity):
        total=Petrol.readFile()
        for i in total:
            if(i[0]==petrol_name):
                i[2]=str(petrol_capacity)
                break
        with open("petrol.txt","w",encoding="utf-8") as file:
            file.write("")
        for i in total:
            if(i[0]==""):
                continue
            with open("petrol.txt","a",encoding="utf-8") as file:
                file.write("{name},{price},{capacity}\n".format(name=i[0],price=i[1],capacity=i[2]))
        return "Updated!"
    #this function checks Petrol Name
    @staticmethod
    def checkPetrolName(petrol_name):
        total=Petrol.readFile()
        result=True
        for i in total:
            if(i[0]==petrol_name):
                result=False
                break
        return result
      #ADD PETROL to FILE
    def addPetrol(self):

        with open("petrol.txt","a",encoding="utf-8") as file:
            file.write("\n")
            file.write(self.__petrol_name+",")
            file.write(self.__petrol_price+",")
            file.write(self.__petrol_capacity+",")
            
        return "Saved!"
            
    
    #show petrol for admin
    @staticmethod
    def showPetrol():
        total=Petrol.readFile()
        #print(total)
        for t in total:
            if(t[0]==''):
                continue

            print("Petrol name:{}\nPetrol price: {}\nPetrol Capacity: {} ".format(t[0],t[1],t[2]))
            print()
                        
        return "--------------------------------------------"
    #show petrol for user
    @staticmethod
    def showPetrolforUser():
        total=Petrol.readFile()
        #print(total)
        for t in total:
            if(t[0]==''):
                continue

            print("Petrol name:{}\nPetrol price: {}".format(t[0],t[1]))
            print()
                        
        return "--------------------------------------------"
      
      
    #gettin all data to list from txt file    
    @staticmethod
    def readFile():
        with open("petrol.txt", 'r',encoding="utf-8") as file:
            petrol=file.read()
            petrol_list=petrol.split("\n")
            total=[]
            for i in petrol_list:
                j=i.split(",")
                total.append(j)
                
        return total

    #remove line that user has given from readfile
    @staticmethod
    def removeFromFile(petrol_name):
        total = Petrol.readFile()

        #print(total)

        with open("petrol.txt","w",encoding="utf-8") as file:
            file.write("")

        for i in total:
            if(i[0]==petrol_name):
                total.remove(i)
                #print(total)
                continue
        for i in total:
            if(i[0]==""):
                continue

            with open("petrol.txt","a",encoding="utf-8") as file:
                file.write("{name},{price},{capacity}\n".format(name=i[0],price=i[1],capacity=i[2]))
        
        return "Removed"
      
   