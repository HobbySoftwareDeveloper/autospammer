#Copyright (c) HobbySoftwareDeveloper 2023-2024, All rights reserved.

import pyautogui
import time

print('Copyright (c) HobbySoftwareDeveloper 2023-2024, All rights reserved.')
print('close this Window or press alt+f4 to exit')

def main():

	while True:

		msg = input("Enter the message: ")
		i = input("How many times ?: ")

		if int(i) < 500:
			pass

		else:
			if input("WARNING! If you write a number that is to big, your computer might die, do you want to continue? (y/n)") == "n":
				main()

			else:
				pass		

		count = input("countdown in seconds: ")

		while(int(count) != 0):
			print(count)
			time.sleep(1)
			count = int(count)-1

		print("FIRE IN THE HOLE!")

		for i in range(0,int(i)):
			pyautogui.typewrite(msg + '\n')

		input("press any key to continue:")

main()