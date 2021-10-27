def dayconverter():
#to input seconds, minutes, hours
    def time():
        s= float(input("Enter number of seconds: "))
        m= float(input("Enter number of minutes: "))
        h= float(input("Enter number of hours: "))
        return s,m,h
    s, m, h = time()
#to obtain days from minutes, hours, formula using return
    def getdays(s, m, h):
        return ((s)+(m*60)+(h*3600))/86400
    days = getdays(s,m,h)
    
    print ("The number of days is", format(days, '.4f'))
dayconverter()