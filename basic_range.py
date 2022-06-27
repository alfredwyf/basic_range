import random
# random is default function in python, generate random number

for i in range(100):
	r = random.randint(1, 1000)
	print(r, "is the", i + 1, "times random number generated")