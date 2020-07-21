def unit_checker():

    unit_tocheck = input("What is the unit of the length? ").lower()

    # Abbreviation lists
    centimeter = ["cm", "centimeter"]
    meter = ["m", "M", "Meter", "METER"]
    inch = ["inch", "in"]
    feet = ["feet","ft"]
    yard = ["yard", "yd"]
    kilometer = ["km", "kilometer"]
    mile = ["mile", "mi"]
    millimeter = ["mm", "millimeter"]

    if unit_tocheck == "":
        print("you chose {}".format(unit_tocheck))
        return unit_tocheck
    elif not unit_checker():
        print("not available unit")

    elif unit_tocheck.lower() in centimeter:
        return "cm"
    elif unit_tocheck.lower() in meter:
        return "m"
    elif unit_tocheck.lower() in inch:
        return "in"
    elif unit_tocheck.lower() in feet:
        return "ft"
    elif unit_tocheck.lower() in millimeter:
        return "mm"
    elif unit_tocheck.lower() in yard:
        return "yd"
    elif unit_tocheck.lower() in kilometer:
        return "km"
    elif unit_tocheck.lower() in mile:
        return "mi"

# ****** Main Routine Goes Here ********
unit_central = {
    "cm": 1,
    "mm": 0.1,
    "m": 100,
    "in": 2.54,
    "ft": 30.48,
    "yd": 91.44,
    "km": 100000,
    "mi": 160934
}
keep_going = ""
while keep_going == "":
    try:
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
    except ValueError:
        print("Not available factor or unit")
        continue

