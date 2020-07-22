# Initialised lists
item_cost = []
expanses = []

# Get inputs and add to item_cost list
item = ""
while item.lower() != "xxx":
    item_cost = []
    item = input("Item Name: ")

    # If the user enters the exit code, break out of the loop
    if item.lower() == "xxx":
      break

    # Get the cost (replace with number checking function in due course)
    cost = float(input("Item Cost: $"))
    costs = ("${:.2f}".format(cost))

    # Add item name and cost to 'item' list
    item_cost.append(item)
    item_cost.append(costs)

    expanses.append(item_cost)

for item in expanses:
    print("{} : {}".format(item[0], item[1]))
