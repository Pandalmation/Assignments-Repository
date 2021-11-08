import math
def hexagonarea(s):
     return ((3 * math.sqrt(3)*(s**2))/2) 
result=0
s= float(input("Enter the side length of the hexagon: "))
if s>0 : print("The area of a hexagon with side length",s,"is","{0:.3f}".format(hexagonarea(s)))
