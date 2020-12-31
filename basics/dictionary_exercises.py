my_dict = {1: "one", 3: "three", 2: "two", "name": "numbers"}

print(my_dict)

print(my_dict[3])

for key in my_dict.keys():
    print(key, my_dict[key])

my_dict = {True: "True", False: "False"}
print(my_dict[0])

my_dict = {(1, 2): "Sai"}
print(my_dict)

print(my_dict[(1, 2)])

# for count in range(23):
#    print(count)

my_list = range(23)
print(my_list)

for count in my_list:
    print(count)

# --------
my_tuple = 1, 2, "3"

a, b, c = my_tuple
print(c)

# ---------------

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    # Write your code here.
    # print(type(item))
    for element in item:
        d3[element] = item[element]

print(d3)

# -------------------------------

colors = (("green", "#008000"), ("blue", "#0000FF"))

# Write your code here.
colors_dictionary = {}

for element in colors:
    #    a, b = element
    colors_dictionary.update({element[0]: element[1]})

print(colors_dictionary)

# --------------------------

tup = (1,) + (1,)
tup = tup + tup
print(len(tup))


# ---------------------------





