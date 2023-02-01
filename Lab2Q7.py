check_list = ['Python','is','the','best']

check_str = input('Enter the string for check : ')

print('The original string is ' + str(check_list))

res = False

for i in check_list:
    if(i.find(check_str)!=-1):

        res = True

print('Is the string is a part of the string list: ' + str(res))

