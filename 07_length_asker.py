
# Get inputs and add to item_cost list


def not_blank(question):

    valid = False
    while not valid:
        response = input(question)
        if response == "":
            print("please enter a valid unit")
            print()
            continue
        else:
            return response

unit = not_blank(" What is the general unit for your shape? ")
area_unit = "{}^2".format(unit)

print(unit)
print(area_unit)