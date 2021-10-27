
def converttemp():
    #input temperature in Farenheit + convert to celcius formula)
    Tf= eval(input("Enter a temperature in Farenheit: "))
    Tc= (5/9)*(Tf-32)
    #farenheit, convert to celcius and convert to kelvin function
    def Farenheit():
        print("The temperature in Farenheit is: ",(Tf))
        return
    def converttocelcius():
        print("The temperature in Celcius is: ",((5/9)*(Tf-32)))
        return
    def converttokelvin():
        print("The temperature in Kelvin is: ",Tc+273.15)
        return
    Farenheit()
    converttocelcius()
    converttokelvin()   
converttemp()
    


    

