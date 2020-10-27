print("hello RAfi")
name = "My name is Rafi"
length = len(name)
print (length)

name = "my name is rafi"
upper_case = name.upper()
print(upper_case)
print(name.lower())
print(name.find("i"))
replace = name.replace("my","Amar")
print(replace)


name= 'Mezbah Uddin Rafi'
is_valid = 'Mezvbah' in name
print(is_valid)

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 ** 3)

x = 10
x *= 3
print(x)

x= 2.6
round = round(x)
print (round)


x= -2.9
abso = abs(x)
roun = round(abso)
print (roun)


import math
x= 2.9
print (math.floor(x))

is_hot= False
is_cold = False

if is_hot:
    print("it is a hot day")

elif is_cold:
    print("it is a cold day")

else:
    print("it is a lovely day")

print("Enjoy your day")

house_price = 10000
good_credit = True

if good_credit:
    amount = house_price * 0.1
    print(amount)

else:
    amount = house_price * 0.2
    print (new_amount)

print (f"Your down payment is:[${amount}]")