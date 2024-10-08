class librarie:
    def show(self):
        print("<<..Books..>>")
        print("===========================================================")
        books = ["GOOD To Great"," rich Dad Poor Dad"," meditations"," My personal MBA","learn in first 20 hours"]
        for i,index in  enumerate(books, start=1):
            print(i,index)

       
        print("")
        print("=================================================")


    def member(self):
        print("================MemberShip======================")
    

        member_op = input("Do you want to member of the library (y/n) ? : ").lower()
        if member_op == "y":
            print("please Enter the details below  :  ")
            name_memb = input("Entert the name : ")

            age_memb = int(input("Enter your age : "))
            if age_memb>=18:
                print("your are eligble for library membership ")
            elif age_memb<18 :
                print("your not Eligible for library menbership ")
                quit() 
            else:
                print("Invaild Input , please give correct age..") 

            proff_memb = input("Enter the (Student/Working professional) : ")

            details = {"NAME":name_memb,
                       "AGE":age_memb,
                       "PROFFESSIONAL":proff_memb}
            for detail,pair  in details.items():
                user_info = print(f' {detail} : {pair}')
                return user_info
            
            return user_info    
                
        elif member_op == "n":
            print("thank you visting the library...")
        else:
            print("Invaild Input , please choose (y/n).. otherwise see the books")        



    def cancel_member(self,user_info):
        print("================? MemberShip_Cancel ?======================")

        member_op1 = input("Do you want to Cancel the MemberShip of the library (y/n) ? : ").lower()

        if member_op1 == "y":
            print("please Enter the details below  :  ")
            print(f' data : {user_info}')
            
        


    def take_book(self):
        self.show()
        books = ["good to great"," rich dad poor dad"," meditations"," my personal mba","learn in first 20 hours"]
        
        try:
            take_book = int(input("Enter the number of the book you want to take: "))
            if 1 <= take_book <= len(books):
                print(f"You have successfully taken the book: {books[take_book - 1]}")
            else:
                print("Invalid input. Please select a valid number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

     
            
        
        

    def init(self):
        while True:
            
    
            print("=================================================")
            print("<<Welcome to the library system >>")
            print("=================================================")

            print("Please choose the Option Below")
            print()
            options = ["1. Show the Books... ","2.Take Book... ","3. Member of the of the librarie... ","4. Cancel the membership ... ","5. EXIT "]
            for i in options:
                print(i)

            print("----------------------------------------")
            choice = int(input("Enter the option : " ))
            print("----------------------------------------")

            

            if choice ==1:
                self.show()
            elif choice==2:
                self.take_book()
            elif choice == 3:
                self.member()
            elif choice == 4:
                self.cancel_member()
            elif choice == 5:
                print("Thank You .. for visting the librarie..")
                quit()    
            else:
                print("Invalid Input ..")
                self.init()




s1 = librarie()
s1.init()


    