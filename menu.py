class Menu:
    #show Menu for admin
    @staticmethod
    def showMenuforAdmin():
        return("""
            1.Add UserAdmin
            2.Add Petrol
            3.Delete Petrol
            4.Add fast Food
            5.Delete fast food
            q.Exit
                  """)
        print()
    #show Menu for user
    @staticmethod
    def showMenuforUser():
        return("""

                  1.1 Oil Station
                  1.2 Cafe
                  
                  """)