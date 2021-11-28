#########################
#Author: Kuleshova Yana
#Date: 28/11/2021
#Task: HW to L7_1
#########################

def mysplit(str):  
    str = "To be or not to be, that is the questions"      
    str_1 = []
    tmp = ''
    for c in str:
        if c == ' ':
            str_1. append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        str_1.append(tmp)
    print(str_1)


print(mysplit("To be or not to be, that is the questions"))
print(mysplit("To be or not to be,that is the questions"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))