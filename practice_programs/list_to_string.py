def list_string(list):
    result= ""
    for element in list:
        result+=str(element)

    return result

print(list_string([1,2,3,4,4,5,6,6,7,8]))    
