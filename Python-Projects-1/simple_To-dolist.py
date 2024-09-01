tasks = []

def addtask():
      task = input("please enter the task :")
      tasks.append(task)
      print(f"Task '{task}' added to the list. ")



def listtask():
     print("here the tasks are i your list...")
     if not tasks:
          print("No task are there")
     else:
          for index,task in enumerate(tasks):
               print(f"task 2'{index}. {task} ' ")     



def deletetask():
     listtask()
     try:
          tasktodelete = int(input("entet the no to delete "))
          if tasktodelete>=0 and tasktodelete<len(tasks):
               tasks.pop(tasktodelete)
               print(f"the task '{tasktodelete}' is deleted ")
     
          else:
               print(f"the '{tasktodelete}'is not found")
     except:
          print("Invalid input")        




if __name__ == '__main__':
    print("welcome to the to-do list program")

    while True:
        print("\n")
        print("please select the following choices")
        print("====================================")
        print("1.Add tasks")
        print("2.delete tasks")
        print("3.list tasks")
        print("4.quit")

        
        choice = int(input("Enter the choices :"))

        if choice==1:
            addtask()

        elif choice==2:
            deletetask()
        
            
        elif choice==3:
             listtask()
            
            
        else:
            print("..Thank you..") 
            quit()           



