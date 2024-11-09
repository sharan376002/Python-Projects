import time 
def timefun():
    start_time = time.time()
    s=0
    for i in range(1, s+1):
        s += i

    name = input("Enter Your Name : ")
    age = int(input("Enter your age : "))


    end_time = time.time()
    return s, end_time-start_time, name, age

excution_time = timefun()

print(excution_time)


