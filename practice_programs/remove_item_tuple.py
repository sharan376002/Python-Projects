# to remove the item from the tuple by using sluicing and concert in to list \

t1 = (1,22,33,44,55,6,66)
print(t1)
new_tuple = t1[:4] + t1[5:]
print(new_tuple)

#by using list conversion

t2 = (1,22,33,44,55,6,66)
print(t2)
new_list = list(t2)
print(new_list)
new_list.remove(55)
new_list = tuple(new_list)
print(new_list)

