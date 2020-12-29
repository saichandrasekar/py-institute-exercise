print(2 == 2.)

print(round(-34.343,1))

if 1:
    print("yes it is true")

#--------------------------------

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

#guess_number = int(input())

#while guess_number != secret_number:
#    print("Ha ha! You're stuck in my loop!")
#    guess_number = int(input())

#print("Well done, muggle! You are free now.")

for i in range(2, 8):
    print("The value of i is currently", i)

#---------------------------------
import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)
for i in range(1,6):
    print(i,"Mississippi")
    #time.sleep(1)
# Write a print function with the final message.
print("Ready or not, here I come!")

#---------------------------------
#while i in range(3):
#    print(i)

#c0 = int(input("Enter a number"))
c0 = 124
counter = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
    else:
        c0 = c0 * 3 + 1
    print(c0)
    counter += 1

print("steps =",counter)

#--------------------------------------------------

#Excercise 1

for i in range(1, 11):
    # Line of code.
    if i % 2 != 0:
        print(i)
        # Line of code.

#--------------------------------------

#Exercise 2

x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

#---------------------

#Exercise 3
name = ""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    name += ch
print(name)

#---------------------------------

#Exercise 4
mod_digits = ""
for digit in "0165031806510":
    if digit == "0":
        mod_digits += "x"
    else:
        mod_digits += digit
print(mod_digits)

#--------------------------------

# Exercise 5
n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

#--------------------------------

# Exercise 6

n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

#-----------------------------

# Exercise 7

for i in range(0, 6, 3):
    print(i)


#----------------------------------
print("Bitwise neg starts")
for count in range(20):
    print(~count)

print(14041987 & 14071950)
print(14041987 & 13041956)
print(14041987 & 19091992)

print(14041987 | 14071950)
print(14041987 | 13041956)
print(14041987 | 19091992)

print(14041987 ^ 14071950)
print(14041987 ^ 13041956)
print(14041987 ^ 19091992)

i = 32838043
for count in str(i):
    print(count)

#-----------------

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

#-----------------

x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2
print(a, b, c, d, e, f)


print(range(5))

#-------------------
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)

#----------------
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

#----------------------

lst = []
del lst
#print(lst)

#-------------------

lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))

lst = ["D", "F", "A", "Z"]
lst.sort()

print(lst)

a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst)

a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()

print(lst)