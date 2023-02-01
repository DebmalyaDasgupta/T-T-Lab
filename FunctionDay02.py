# def changeme(mylist):
#     mylist.append([1, 2, 3, 4])
#     print("Values inside the function: ", mylist)
#     return
#
# mylist = [10, 20, 30]
# changeme(mylist)
# print("Values outside the function: ", mylist)


total = 0

def sum(arg1,arg2):
    total = arg1 + arg2
    print("Inside the function local total is : ", total)
    return total

sum(10,20)
print("Outside the function global total : ", total)

