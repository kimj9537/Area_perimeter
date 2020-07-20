# Initialised lists
length_unit = []
expanses = []

# Get inputs and add to item_cost list
item = ""
while length_unit != "xxx":
    length_unit = []
    unit = input(" Unit: ")

    # If the user enters the exit code, break out of the loop
    if unit.lower() == "xxx":
      break

    # Get the cost (replace with number checking function in due course)
    length = float(input("Length: "))
    lengths = ("${:.2f}".format(length))

    # Add item name and cost to 'item' list
    length_unit.append(item)
    length_unit.append(length)

    expanses.append(length_unit)

for line_name in expanses:
    print("{} : {}".format(length_unit[0], length_unit[1]))
