
# Declaring dictionary 
dict = {'Name':'Zara','Age':7,'Class':'First'}

#Accessing Dictionary
print(dict['Name']);
print(dict['Age']);

#Updating Dictionary
dict['Age'] = 8
dict['School'] = "DPS School"

#Deletion from Dictionary

del dict #remove all dictionary
del dict['Name'] #remove all entries with key name 
dict.clear()

# Note : More than one entry per key is not allowed 
# Means : When duplicate keys are encountered durring assignment the last assignment wins