def calc_weight_on_planet(weightearth,surfacegravity=23.1):
#formula to find mass
    mass = weightearth/9.8
    weightonplanet= mass*surfacegravity
    print(weightonplanet)
    return
#calling out functions
calc_weight_on_planet(120, 9.8)
calc_weight_on_planet(120)
calc_weight_on_planet(120, 23.1)
