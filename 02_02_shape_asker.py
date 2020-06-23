def shape_name_checker():

  valid = False
  while not valid:
    response = input("What is the name of the shape?")

    if response == "c" or response == "C" or response == "Circle" or response == "CIRCLE":
      return "circle"
    elif response =="s" or response == "S" or response == "Square" or response == "SQUARE":
      return "square"
    elif response == "r" or response == "R" or response == "Rectangle" or response == "RECTANGLE":
      return "rectangle"
    elif response == "t" or response == "T" or response == "Triangle" or response == "TRIANGLE":
      return "triangle"
    elif response == "p" or response == "P" or response == "Parallelogram" or response == "PARALLELOGRAM":
      return  "parallelogram"

user_choice = shape_name_checker()
print(user_choice)