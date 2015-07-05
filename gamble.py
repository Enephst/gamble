#!/usr/bin/python3
#python blah blah


import random
import time



umoney = 100
#tmoney = 100
#Maybe do that later??

usmoney = 100

choice = -1

print("Wanna play some dice?")
time.sleep(2)

while umoney > 0 and choice != "1":
	time.sleep(1)
	print("""
Options:
0 - Roll the dice
1 - Exit with winnings	
You have""",umoney,"dollars""")

	choice = input("What are you going to do? <0/1> ")

	if choice == "0":
	
		udie1 = random.randint(1, 6)
		udie2 = random.randint(1, 6)

		utotal = udie1 + udie2

	
		tdie1 = random.randint(1, 6)
		tdie2 = random.randint(1, 6)
	
		ttotal = tdie1 + tdie2

		if ttotal > utotal: 
			mlose = random.randint(1, 10)
			print("You rolled",utotal,"They rolled",ttotal)
			time.sleep(2)
			print("You lose",mlose,"Dollars")
			umoney -= mlose

			
		elif ttotal < utotal:
			ugain = random.randint(1, 10)
			print("you rolled",utotal,"They rolled",ttotal)
			time.sleep(2)
			print("You gain",ugain,"Dollars")
			umoney += ugain


	elif choice == "1":
		print("later!")
		time.sleep(1)
		print("you leave with",umoney,"dollars")
		
		if usmoney > umoney:
			print("You lost money.")
		elif umoney > usmoney:
			print("You gained money.") 	
	
	
	
else:
	input("press enter to leave")











