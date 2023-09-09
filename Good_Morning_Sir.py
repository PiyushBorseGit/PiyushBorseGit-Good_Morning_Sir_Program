import time

timestamp= time.strftime("%H")

print(timestamp)

if (int(timestamp) <12):
	print("Good Mornig Sir")
	
elif(int(timestamp) <6):
	print('Good AfterNoon Sir')

elif(int(timestamp)<24):
	print("Good Evening Sir")
	
else:
	print('Good Night Sir')
	