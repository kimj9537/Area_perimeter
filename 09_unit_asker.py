def unit_checker(question):

    unit_to_check = input("What is the unit that you are going to use? ").lower()

    # Abbreviation lists
    centimeter = ["cm", "centimeter"]
    meter = ["m", "M", "Meter", "METER"]
    inch = ["inch", "in"]
    feet = ["feet","ft"]
    yard = ["yard", "yd"]
    kilometer = ["km", "kilometer"]
    mile = ["mile", "mi"]
    millimeter = ["mm", "millimeter"]

    if unit_to_check == "":
        print("you chose {} as the unit that you are going to use".format(unit_to_check))
        return unit_to_check
    elif not unit_checker():
        print("Not available unit that can be writen in this program.")

    elif unit_to_check.lower() in centimeter:
        return "cm"
    elif unit_to_check.lower() in meter:
        return "m"
    elif unit_to_check.lower() in inch:
        return "in"
    elif unit_to_check.lower() in feet:
        return "ft"
    elif unit_to_check.lower() in millimeter:
        return "mm"
    elif unit_to_check.lower() in yard:
        return "yd"
    elif unit_to_check.lower() in kilometer:
        return "km"
    elif unit_to_check.lower() in mile:
        return "mi"


def not_blank(question):
    error = "This unit can't be used in this program. "

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if response == unit_checker(question):
            print(unit_checker(question))
            continue
        elif not response == unit_checker(question):
            print(error)
            continue