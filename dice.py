# Name: Sean Macarthur
# Period 4
# Dice Rolling Simulator
import random 

xif = int(input("How many times would you like to roll? "))
pif = int(input(" How many six's do you predict will be rolled? "))

x=0
one=0
two=0
three=0
four=0
five=0
six=0
while True:
	dice_num = random.randint(1,6)
	print("Roll#" +str(x) +str(": ") +str(dice_num))
	if dice_num == 1:
		one = one + 1
	elif dice_num == 2:
		two = two + 1
	elif dice_num == 3:
		three = three +1
	elif dice_num == 4:
		four = four +1
	elif dice_num == 5:
		five = five +1
	elif dice_num == 6:
		six = six +1

	x = x +1
	if x == xif:
		break
print("Here are the statisics of dice rolls: ")
print("Ones rolled: " + str(one))
print("Twos rolled: " + str(two))
print("Threes rolled: " + str(three))
print("Fours rolled: " + str(four))
print("Fives rolled: " + str(five))
print("Sixes rolled: " + str(six))
oneP = one/int(xif)*100
twoP = two/int(xif)*100
threeP = three/int(xif)*100
fourP = four/int(xif)*100
fiveP = five/int(xif)*100
sixP = six/int(xif)*100
print("Ones percentage: " + str(oneP) +str("%"))
print("Twos percentage: " + str(twoP) +str("%"))
print("Threes percentage: " + str(threeP) +str("%"))
print("Fours percentage: " + str(fourP) +str("%"))
print("Fives percentage: " + str(fiveP) +str("%"))
print("Six percentage: " + str(sixP) +str("%"))
if pif == int(six):
	print("You actually got it right")
elif pif < int(six):
	print("Too low, the correct amount of sixes rolled was " + str(six))
elif pif > int(six):
	print("Too high, the correct amount of sixes rolled was " + str(six))

