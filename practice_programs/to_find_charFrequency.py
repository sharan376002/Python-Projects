#find the char frequency

def Char_frequency(str):
    dict={}
    for n in str:
        keys =dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n] =1
    return dict

print(Char_frequency("SharanG"))


                