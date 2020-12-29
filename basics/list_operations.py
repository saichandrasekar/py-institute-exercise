print("","0","1","2","3","4","]",sep=" ")
my_list = [1 , 2, 3, 4, 5]

my_new_list = my_list[:]
print(my_new_list)

my_new_list = my_list[1:5]
print(my_new_list)

my_new_list = my_list[2:5]
print(my_new_list)

my_new_list = my_list[0:5]
print(my_new_list)

my_new_list = my_list[:5]
print("empty:5", my_new_list)

my_new_list =my_list[2:4]
print("2:4", my_new_list)

my_new_list = my_list[3:6]
print("3:6", my_new_list)

my_new_list = my_list[3:3]
print("3:3", my_new_list)

my_new_list = my_list[:-2]
print(":-2", my_new_list)

my_new_list = my_list[:2]
print(":2", my_new_list)

my_new_list = my_list[-2:-2]
print("2:-1", my_new_list)

my_new_list = my_list[2: 4]
print("2:4", my_new_list)

my_newlist = my_list[1:2]
print(my_newlist)
print(my_newlist in my_list)
print(2 in my_list)

#---------------------

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)

#--------------------

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)

#-----------------------

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)

#--------------------

list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)

#-------------------------------------

my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)  # outputs True
print("A" not in my_list)  # outputs True
print(3 not in my_list)  # outputs True
print(False in my_list)  # outputs False


#--------------------------

my_list = [1,2,3,4]
print(my_list[-3:-2])

#-------------------

my_list = [[3-i for i in range(3)] for j in range(3)]
for index in range(3):
    for j_index in range(3):
        print(my_list[index][j_index],sep=" ", end="")
    print()
s = 0
for i in range(3):
    s += my_list[i][i]
print(s)

for index in range(-4, -2):
    print(index)