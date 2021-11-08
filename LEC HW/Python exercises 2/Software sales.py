import math
n= eval(input("Enter the number of packages purchased: "))
totalamountwithoutdisc= 99*n

if (n<10):
        disc0= (totalamountwithoutdisc*0)
        print("Discount amount @ 0% : $","{:.2f}".format(disc0))
        print("Total amount after discount: $","{:.2f}".format(totalamountwithoutdisc-disc0))
elif (10<=n<=19):
        disc10= totalamountwithoutdisc*10/100
        print("Discount amount @ 10% : $","{:.2f}".format(disc10))
        print("Total amount after discount: $","{:.2f}".format(totalamountwithoutdisc-disc10))
elif (20<=n<=49):
        disc20= totalamountwithoutdisc*20/100
        print("Discount amount @ 20% : $","{:.2f}".format(disc20))
        print("Total amount after discount: $","{:.2f}".format(totalamountwithoutdisc-disc20))
elif (50<=n<=99):
        disc30= totalamountwithoutdisc*30/100
        print("Discount amount @ 30% : $","{:.2f}".format(disc30))
        print("Total amount after discount: $","{:.2f}".format(totalamountwithoutdisc-disc30))
else: 
        disc40= totalamountwithoutdisc*40/100
        print("Discount amount @ 40% : $","{:.2f}".format(disc40))
        print("Total amount after discount: $","{:.2f}".format(totalamountwithoutdisc-disc40))
