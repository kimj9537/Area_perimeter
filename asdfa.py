import math


def shape_checker(question, to_check):

    valid = False
    while not valid:

        response = input(question).lower()

        for shape in to_check:
            if response == shape:
                return response
            elif response == shape[0]:
                return shape

        print("That isn't a valid shape name.")

# *** Main Routine ****

shape_name = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]

shape_name = shape_checker("What is the name of the shape?", shape_name)
print("You are now asking {}".format(shape_name))


def calculation_kind_checker():

    error = " Please choose one choice for the program to calculate. "

    valid = False
    while not valid:
        response = input("What is the kind of calculation that you want the prgram to do with this shape? ").lower()

        if response == "area" or response == "a":
            return "area"
        elif response == "perimeter" or response == "pm":
            return "perimeter"
        elif response == "both" or response == "b":
            return "both"
        else:
            print(error)

user_choice = calculation_kind_checker()


def num_check(question):

    error = "Please enter a number that is more than zero. "
    error1 = "You've got any of the factors in the program wrongly, so please try again. "

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:

                return response

        except ValueError:
            print(error)

if shape_name == "circle":
    radius = num_check(" How long is the radius? ")
    area_of_circle = radius * radius * math.pi
    perimeter_of_circle = radius * 2 * math.pi
    if user_choice == "both":
        print("The area of the circle is {}".format(area_of_circle))
        print("The perimeter of the circle is {}".format(perimeter_of_circle))
    elif user_choice == "area":
        print("The area of the circle is {}".format(area_of_circle))
    elif user_choice == "perimeter":
        print("The perimeter of the circle is {}".format(perimeter_of_circle))