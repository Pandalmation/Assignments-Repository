import sys
def length(v,a):
    return (float)(v**2)/(a*2)
    
v= eval(input("Enter the plane's take-off speed in m/s: "))
a= eval(input("Enter the plane's acceleration in m/s**2: "))

answer = length(v,a)
dec_answer = "{:.4f}".format(answer)
print("the minimum runaway length needed for this airplane is:", dec_answer)
