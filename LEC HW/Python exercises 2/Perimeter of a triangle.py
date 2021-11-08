import sys
edge1= eval(input("enter length of edge 1: "))
edge2= eval(input("enter length of edge 2: "))
edge3= eval(input("enter length of edge 3: "))

if edge1 + edge2 > edge3:
    if edge2 + edge3 > edge1:
        if edge1 + edge3 > edge2:
            perimeter = edge1 + edge2 + edge3
            print("perimeter: ", perimeter)
else:  
    print("Perimeter cannot be calculated: the input is invalid!")