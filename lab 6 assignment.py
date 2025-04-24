#Assigment
#1
Names=["Asmita",("Het"),"Suhani",("Ani")]
boys_count=0
girls_count=0
for ele in Names:
 if isinstance(ele,tuple):
    boys_count+=1
 else:
    girls_count+=1
print("Number of boys:",boys_count)
print("Number of girls:",girls_count)
#2
Students=[(2,"Asmita",17),
           (3,"Isha",18),
          (4,"Het",19)]
rollno_list=[]
names_list=[]
age_list=[]
for Students in Students:
 rollno_list=[Students[0]]
 name_list=[Students[1]]
 age_list=[Students[2]]
print("Roll no :",rollno_list)
print("Name:",name_list)
print("age:",age_list)



#4
food_items = [('Pizza', 8.99), ('Burger', 5.49), ('Sushi', 12.99), ('Pasta', 7.99), ('Ice Cream', 3.99)]

sorted_food_items = sorted(food_items, key=lambda x: x[1], reverse=True)

print("Food items sorted by price (descending):", sorted_food_items)

#5
tuples_list = [(1, 2), (), (3, 4), (), (5, 6), ()]

filtered_list = [t for t in tuples_list if t]

print("List after removing empty tuples:", filtered_list)

#6
original_tuple = (1, 2, 3, 4, 5)

temp_list = list(original_tuple)
temp_list[2] = 99

modified_tuple = tuple(temp_list)

print("Original tuple:", original_tuple)
print("Modified tuple:", modified_tuple)

#7
original_tuple = (1, 2, 3, 4, 5)

temp_list = list(original_tuple)
del temp_list[2]

modified_tuple = tuple(temp_list)

print("Original tuple:", original_tuple)
print("Modified tuple:", modified_tuple)

#3
date1 = (18, 2, 2025)
date2 = (25, 2, 2025)

date1_formatted = date1(date1[2], date1[1], date1[0])
date2_formatted = date2(date2[2], date2[1], date2[0])

difference = date2_formatted - date1_formatted

print("Number of days between the two dates:", difference.days)
