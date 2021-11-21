#########################
#Author: Kuleshova Yana
#Date: 21/11/2021
#Task: 4_6
#########################

def liters_100km_to_miles_gallon(liters):
    american_mile = 1609.344
    american_gallon = 3.785411784
    gall = liters / american_gallon
    # miles = 100 * 1000 / american_mile
    liters = 100 * american_gallon / gall * american_mile
    return liters

liters_100km_to_miles_gallon()

def miles_gallon_to_liters_100km(miles):
    american_mile = 1609.344
    american_gallon = 3.785411784
    gall = american_mile / american_gallon
    miles = 100 * 1000 / american_mile
    return miles/gall

miles_gallon_to_liters_100km()
