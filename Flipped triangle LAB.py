rows=eval(input("How many rows?"))
for i in range(rows):
  for j in range(i,rows):
    print(" ", end=" ")
  for j in range(i+1):
    print("*",end=" ")
  print()