def shape_name_checker():

  valid = False
  while not valid:
    response = input("What is the name of the shape?").lower()

    if response == "c" or response == "circle":
        return "circle"
    elif response == "s" or response == "square":
        return "square"
    elif response == "r" or response == "rectangle" or response == "rec":
        return "rectangle"
    elif response == "t" or response == "triangle" or response == "tri":
        return "triangle"
    elif response == "p" or response == "Parallelogram":
        return "parallelogram"

user_choice = shape_name_checker()
print(user_choice)