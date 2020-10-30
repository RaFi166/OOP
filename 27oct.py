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

logical operator
has_good= True
has_beter= False
if has_beter and has_good:
    print("you are right")
else:
    print("yo r not good")

tempareture = input("Enter the temparature here: ")

if int(tempareture) > 30:
    print ("it is a hot day")

else:
    print ("it is not a hot day")

name = input ("Write down your name at here: ")
if len(name) < 3 :
    print ("short name")


elif len(name) > 50:
    print("looong name")

else:
    print("perfectoo name")


weight converter program


weight = input("Enter your weight here: ")
convert = input(" l(bs) or kg(s): ")


if convert == "l" :
    print(0.5 * int(weight))

else:
    print(1 * int(weight))


i =1
while i<=5:
    print(i * '*')
    i= i + 1
print ("OK done")


numbers = [10, 20,100, 50, 40,60, 90]
max_number= numbers[0]

for number in numbers:
    max_number > number
    max_number_latest = max_number
    
