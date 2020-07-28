
# Get inputs and add to item_cost list


def not_blank(question):
    error = "The length has to be bigger than 0. "
    valid = False
    while not valid:
        while not valid:
            response = input(question)
            if response == "":
                print()
                continue
            else:
                return response

unit = not_blank(" What is the general unit for your shape? ")
area_unit = "{}^2".format(unit)

print(unit)
print(area_unit)