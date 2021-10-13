import sys
subtotal= float(input("Enter the subtotal: $"))
tipamount= int(input("Enter tip amount (as a %): "))
tip= (float)(subtotal)*(tipamount)/100

answer= "$",tipamount
print("Subtotal: $","{:,.2f}".format(subtotal))
print("tip: $","{:,.2f}".format(tip))
print("Total: $","{:,.2f}".format(tip + subtotal))

