# dict = {}
# dict["one"] = "This is one"
# dict[2] = "This is two"
#
# tinydict = {'name':"John",'code':6734,'dept':"sales"}
#
# print(dict["one"])
# print(dict[2])
# print(tinydict)
# print(tinydict.keys())
# print(tinydict.values())


employee_1 = {'name':'Bob','id': 8976,'salary':25000,'DOJ':'12thJan2020'}
employee_2 = {'name':'Rob','id': 4578,'salary':28000,'DOJ':'18thJan2021'}
employee_3 = {'name':'Jason','id': 7865,'salary':35000,'DOJ':'20thFeb2022'}
employee_4 = {'name':'Bryan','id': 2345,'salary':18000,'DOJ':'13thMar2021'}

# print(employee_1)
# print(employee_2)
# print(employee_3)
# print(employee_4)

nested_dict = {'employee_1': {'name':'Bob','id': 8976,'salary':25000,'DOJ':'12thJan2020'},
               'employee_2' : {'name': 'Rob', 'id': 4578, 'salary': 28000, 'DOJ': '18thJan2021'},
               'employee_3' : {'name': 'Jason', 'id': 7865, 'salary': 35000, 'DOJ': '20thFeb2022'},
               'employee_4' : {'name': 'Bryan', 'id': 2345, 'salary': 18000, 'DOJ': '13thMar2021'}
              }

print(nested_dict.keys())
print(nested_dict.values())
print(len(nested_dict))
print(len(employee_4))