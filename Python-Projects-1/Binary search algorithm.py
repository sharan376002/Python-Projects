# a function that takes a list and target parameter 
# multiple variable : middle , start , end , steps 
# recursion or while loop
# increase the steps each time a split is done 
# condition to track target position  , when greater than middle value or lower than middle value



def binary_search(list , element):
    middle = 0 
    start = 0
    end = len(list)
    steps = 0 


    while (start<=end):
        print("steps",steps ,":", str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle -1
        else:
            start = middle +1
    return -1        


my_list = [10,20,30,40,50,60,70,80,90,100]
target = 10

binary_search(my_list, target)


print("linear search")

my_list2 = [1,45,65,768,45,4,8,34,23,56,8,99,100]

for i in my_list2:
    if i==100:
        print(i, "found")




        








































