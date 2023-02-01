
D = { "A1" : "KII",  "A2" : "IIT", "A3" : "ABC" , "A4" : "T" }

# Python3 code to demonstrate working of
# Substring Key match in dictionary
# Using items() + list comprehension

# initializing search key string
search_key = 'KIIT'

# printing original dictionary
print("The original dictionary is : " + str(D))

res = [val for key, val in D.items() if search_key in key]

# printing result
print("Values for substring keys : " + str(res))
