import math
def angle(m,g,f):
        return math.degrees(math.asin(f/(m*g)))
result=0
g= 9.8;"m/s**2"
m=float(input("Enter the mass of the cart (in kg): "))
f=float(input("Enter the force to push the cart (in N): "))
if m>0 or m==0 : print("The angle of the ramp is","{:.1f} degrees".format(angle(m,g,f)))
