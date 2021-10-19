class User:
    def __init__(self,username,password):
        self.setUsername(username)
        self.setPassword(password)


    def setUsername(self,username):
        self.__username=username
    def getUsername(self):
        return self.__username
      

    def setPassword(self,password):
        self.__password=password
    def getPassword(self):
        return self.__password

#function for useradmin
    def addUser(self):
        with open("credentials.txt","a",encoding="utf-8") as file:
            file.write("\n")
            file.write(self.__username+",")
            file.write(self.__password+",")
           
        return "Saved!"


#to create list for username and password
    @staticmethod
    def getUsers():
        with open("credentials.txt","r",encoding="utf-8") as file:
            user=file.read()
            user_list=user.split("\n")
            total=[]
            for i in user_list:
                j=i.split(",")
                total.append(j)
        return total