
# Declearing set
Days = set(["Mon","Tue","Web","Thu","Fri","Sat"])
Months = {"Jan","Feb","Mar","Apr","May","Jun"}
Dates = {21,22,23}
print(Days)
print(Months)
print(Dates)

# Accessing Values in a set
for day in Days :
    print(day)

#Adding values in a set 
Days.add("Sun")

#Removing values from a set
Days.discard("Sun")


#Union of two sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)


#Intersection of two sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays)


#Difference of a sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB
print(AllDays)

#Subsets and Supersets 
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)