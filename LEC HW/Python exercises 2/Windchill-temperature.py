import sys
def windchilltemperature(ta,v):
    return(float(35.74 + (0.6215*ta) - (35.75*v**0.16) + (0.4275*ta*v**0.16)))

ta= eval(input("Enter the temperature between -58 degrees Farenheit and 41 degrees Farenheit: "))

while True:
    if (-58<ta<41) :
        break
    else: 
        ta=eval(input("Temperature must be between -58F and 41F. Please re-enter the temperature: "))
        continue

v= eval(input("Enter the windspeed greater than or equal to 2mph: "))
while True:
    if (v>=2): 
        break
    else: 
       v=eval(input("Speed must be greater or equal to 2. Please re-enter the wind speed: "))
       continue

print("The wind-chill temperature is ","{:,.3f}".format(windchilltemperature(ta,v)))