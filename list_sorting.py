# Find 1st place,2nd place,3rd place of these running racers
# Name = ['stephen','muthu','celin','rajarajan']
# Time = [18,22.3,19.1,17.2]
names = ['stephen','muthu','celin','rajarajan']
seconds = [18,22.3,19.1,17.2]
time = []

for x in seconds:
    for y in seconds:
        if x>y:
