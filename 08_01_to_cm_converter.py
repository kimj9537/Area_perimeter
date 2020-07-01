def unit_checker():

    unit_tocheck = input("What is the unit of the length? ")

    # Abbreviation lists
    centimeter = ["cm", "CM", "Centimeter", "CENTIMETER"]
    meter = ["m", "M", "Meter", "METER"]
    inch = ["Inch", "in", "IN", "INCH"]
    feet = ["Feet","ft" ,"FT", "FEET"]
    yard = ["Yard", "yd", "YD", "YARD"]
    kilometer = ["km", "KM", "Kilometer", "KILOMETER"]
    mile = ["Mile", "mi", "MI", "MILE"]
    milimeter = ["mm", "MM", "Milimeter", "MILIMETER"]

    if unit_tocheck == "":
        print("you chose {}".format(unit_tocheck))
        return unit_tocheck

    elif unit_tocheck == "CM" or unit_tocheck.lower() in centimeter:
        return "cm"
    elif unit_tocheck == "M" or unit_tocheck.lower() in meter:
        return "m"
    elif unit_tocheck == "IN" or unit_tocheck.lower() in inch:
        return "in"
    elif unit_tocheck == "FT" or unit_tocheck.lower() in feet:
        return "ft"
    elif unit_tocheck == "MM" or unit_tocheck.lower() in milimeter:
        return "mm"
    elif unit_tocheck == "YD" or unit_tocheck.lower() in yard:
        return "yd"
    elif unit_tocheck == "KM" or unit_tocheck.lower() in kilometer:
        return "km"
    elif unit_tocheck == "MI" or unit_tocheck.lower() in mile:
        return "mi"

# ****** Main Routine Goes Here ********
unit_central = {
    "cm": 1,
    "mm": 0.1,
    "m": 100,
    "inch": 2.54,
    "feet": 30.48,
    "milimeter": 10,
    "yard": 91.44,
    "kilometer": 100000,
    "mile": 160934
}
keep_going = ""
while keep_going == "":
    amount = eval(input("How big is the factor? "))
    amount = float(amount)

    # Get unit and change it to match dictionary.
    unit = unit_checker()
    print("unit", unit)

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("Amount in cm is {}".format(amount))

    keep_going = input("<enter> or q ")
