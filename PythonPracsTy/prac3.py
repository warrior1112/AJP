import random

n1 = random.randrange(1,10);
n2 = random.randrange(1,17);
if(n1>n2):
	if(n1>5):
		print('greater than 5')
	else:
		('greater than n2 but not greater than 5')
else:
	print('less than n2')

if(n2>n1):
	print("n2 is greater")
else:
	print("n1 is greater")

if(n2>n1):
	print("n1 is best")
elif(n2>(n1+2)):
	print("pretty cool!")
else:
	print('n2 is best')