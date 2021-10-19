class Food:
    def __init__(self,food_id,food_name,food_price,food_number):
        self.setFoodName(food_name)
        self.setFoodPrice(food_price)
        self.setFoodNumber(food_number)
        self.setFoodID(food_id)


    def setFoodName(self,food_name):
        self.__food_name=food_name
    def getFoodName(self):
        return self.__food_name

    def setFoodID(self,food_id):
        self.__food_id=food_id
    def getFoodID(self):
        return self.__food_id    
      

    def setFoodPrice(self,food_price):
        self.__food_price=food_price
    def getFoodPrice(self):
        return self.__food_price
    

    def setFoodNumber(self,food_number):
        self.__food_number=food_number
    def getFoodNumber(self):
        return self.__food_number
    #this function checks Food ID
    @staticmethod
    def checkFoodID(food_id):
        total=Food.readFile()
        result=True
        for i in total:
            if(i[0]==food_id):
                result=False
                break
        return result
    #this function update food count
    @staticmethod
    def updateNumber(food_id,food_number):
        total=Food.readFile()
        for i in total:
            if(i[0]==food_id):
                i[3]=str(food_number)
                break
        with open("food.txt","w",encoding="utf-8") as file:
            file.write("")
        for i in total:
            if(i[0]==""):
                continue
            with open("food.txt","a",encoding="utf-8") as file:
                file.write("{id},{name},{price},{number}\n".format(id=i[0],name=i[1],price=i[2],number=i[3]))
        return "Updated!"
      
      #ADD Food to Food FILE
    def addFood(self):
        with open("food.txt","a",encoding="utf-8") as file:
            file.write("\n")
            file.write(self.__food_id+",")
            file.write(self.__food_name+",")
            file.write(self.__food_price+",")
            file.write(self.__food_number)
       
        return "Saved!"
   
    #show food for user
    @staticmethod
    def showFood():
        total=Food.readFile()
        #print(total)
        for t in total:
            if(t[0]==''):
                continue

            print("Food ID:{}\nFood Name: {}\nFood Price: {}\nFood number: {}".format(t[0],t[1],t[2],t[3]))
            print()
                        
        return "--------------------------------------------"
    #show food for user. We dont show food count to user
    @staticmethod
    def showFoodforUser():
        total=Food.readFile()
        #print(total)
        for t in total:
            if(t[0]==''):
                continue

            print("Food ID:{}\nFood Name: {}\nFood Price: {}\n".format(t[0],t[1],t[2]))
            print()
                        
        return "--------------------------------------------"
      
      
    #getting all data from txt file
    @staticmethod
    def readFile():
        with open("food.txt", 'r',encoding="utf-8") as file:
            food=file.read()
            food_list=food.split("\n")
            total=[]
            for i in food_list:
                j=i.split(",")
                total.append(j)
                
        return total

    #remove line that user has given from readfile
    @staticmethod
    def removeFromFile(UID):
        total = Food.readFile()

      #  print(total)

        with open("food.txt","w",encoding="utf-8") as file:
            file.write("")

        for i in total:
            if(i[0]==UID):
                total.remove(i)
                #print(total)
                continue
        for i in total:
            if(i[0]==""):
                continue

            with open("food.txt","a",encoding="utf-8") as file:
                file.write("{ID},{name},{price},{count}\n".format(ID=i[0],name=i[1],price=i[2],count=i[3]))
        
        return "Removed"
      