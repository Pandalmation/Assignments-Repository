#input width, height and desired width using calcnewheight function
def calcnewheight():
    currentwidth=eval(input("Enter the current width: "))
    currentheight=eval(input("Enter the current height: "))
    desiredwidth=eval(input("Enter the desired width: "))
#aspect ratio + corresponding height formula using known variables
    aspectratio= currentheight/currentwidth
    correspondingheight= (aspectratio*desiredwidth)
    return (correspondingheight)
    
print("The corresponding height is: ".format(), calcnewheight())
