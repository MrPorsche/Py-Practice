import time
timestamp = time.strftime('%H:%M:%S')

hour = int(time.strftime('%H'))

if hour >= 5 and hour < 12:
    print("Good Morning!")
elif hour >= 12 and hour < 17:
    print("Good Afternoon!")
elif hour >= 17 and hour < 20:
    print("Good Evening!")
elif hour >= 20 or hour < 5:
    print("Good Night!")
else:
    print("Invalid Time!")

print(timestamp)