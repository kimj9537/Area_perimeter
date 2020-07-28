import math

# this function is to start asking the shape before any functioning.


def num_check(question):

    error = "Please enter a number that is more than zero. "

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

# Function which outputs error if the shape isn't an available one for the program


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

# Function that asks the kinds of values that the user want the program to calculate(area, perimeter, both)


def calculation_kind_checker():

    error = " Please choose one choice for the program to calculate. "

    valid = False
    while not valid:
        response = input("What is the kind of calculation that you want the program to do with this shape? ").lower()

        if response == "area" or response == "a":
            return "area"
        elif response == "perimeter" or response == "pm":
            return "perimeter"
        elif response == "both" or response == "b":
            return "both"
        else:
            print(error)

user_choice = calculation_kind_checker()

# Function that it asks the unit of the lengths for the shapes


def not_blank(question):
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


# *** Main Routine ****
# List of the kind of shapes
shape_name = ["circle", "square", "rectangle", "triangle", "parallelogram"]
# asking the shape and also answering
shape_name = shape_checker("What is the name of the shape?", shape_name)
print("You are now asking {}".format(shape_name))

# calculate area(, perimeter or both) of circle with the factor that the user has given
if shape_name == "circle":
    radius = num_check(" How long is the radius? ")
    area_of_circle = radius * radius * math.pi
    perimeter_of_circle = radius * 2 * math.pi
    if user_choice == "both":
        print("The area of the circle is {} {}^2. ".format(area_of_circle, unit))
        print("The perimeter of the circle is {} {}. ".format(perimeter_of_circle, unit))
    elif user_choice == "area":
        print("The area of the circle is {} {}^2. ".format(area_of_circle, unit))
    elif user_choice == "perimeter":
        print("The perimeter of the circle is {} {}. ".format(perimeter_of_circle, unit))
# calculate area(, perimeter or both) of square with the factor that the user has given
if shape_name == "square":
    side_length = num_check(" How long is the length of a side of the square? ")
    area_of_square = side_length * side_length
    perimeter_of_square = side_length * 4
    if user_choice == "both":
        print("The area of the square is {} {}^2".format(area_of_square, unit))
        print("The perimeter of the square is {} {}".format(perimeter_of_square, unit))
    elif user_choice == "area:":
        print("The area of the square is {} {}^2. ".format(area_of_square, unit))
    elif user_choice == "perimeter":
        print("The perimeter of the square is {} {}. ".format(perimeter_of_square, unit))
# calculate area(, perimeter or both) of rectangle with the factor that the user has given
if shape_name == "rectangle":
    base_length = num_check("How long is the base length of the rectangle? ")
    height_length = num_check("How long is the height length of the rectangle? ")
    area_of_rectangle = base_length * height_length
    perimeter_of_rectangle = (base_length + height_length) * 2
    if user_choice == "both":
        print("The area of the rectangle is {} {}^2. ".format(area_of_rectangle, unit))
        print("The perimeter of the rectanlge is {} {}. ".format(perimeter_of_rectangle, unit))
    elif user_choice == "area:":
        print("The area of the rectangle is {} {}^2. ".format(area_of_rectangle, unit))
    elif user_choice == "perimeter":
        print("The perimeter of the rectangle is {} {}. ".format(perimeter_of_rectangle, unit))
# calculate area(, perimeter or both) of triangle with the factor that the user has given
if shape_name == "triangle":
    height_length = num_check(" How long is the height of this triangle? ")
    base_length = num_check(" How long is the base of the triangle? ")
    # asks different lengths of sides since triangle needs different kind of lengths to calculate
    # each area and perimeter
    side_A_length = num_check(" How long is the side A of this triangle? ")
    side_B_length = num_check(" How long is the side B of this triangle? ")
    side_C_length = num_check(" How long is the side C of this triangle? ")
    area_of_triangle = height_length * base_length * 0.5
    perimeter_of_triangle = side_A_length + side_B_length + side_C_length
    if user_choice == "both":
        print("The area of the triangle is {} {}^2. ".format(area_of_triangle, unit))
        print("The perimeter of the triangle is {} {}. ".format(perimeter_of_triangle, unit))
    if user_choice == "area":
        print("The area of the triangle is {} {}^2. ".format(area_of_triangle,unit))
    if user_choice == "perimeter":
        print("The perimeter of the triangle is {} {}. ".format(perimeter_of_triangle, unit))
# calculate area(, perimeter or both) of parallelogram with the factor that the user has given
if shape_name == "parallelogram":
    base_length = num_check(" How long is the base of this parallelogram? ")
    height_length = num_check(" How long is the height of this parallelogram? ")
    # also asks other lengths like triangle since it needs other lengths are needed for
    # calculation of perimeter compared to area
    side_A_length = num_check(" How long is the side A of this parallelogram? ")
    side_B_length = num_check(" How long is the side B of this parallelogram? ")
    side_C_length = num_check(" How long is the side C of this parallelogram? ")
    side_D_length = num_check(" How long is the side D of this parallelogram? ")
    perimeter_of_parallelogram = side_A_length + side_B_length + side_C_length + side_D_length
    area_of_parallelogram = base_length * height_length
    if user_choice == "both":
        print("The area of the parallelogram is {} {}^2. ".format(area_of_parallelogram, unit))
        print("The perimeter of the parallelogram is {} {}. ".format(perimeter_of_parallelogram, unit))
    if user_choice == "area":
        print("The area of the parallelogram is {} {}^2. ".format(area_of_parallelogram, unit))
    if user_choice == "perimeter":
        print("The perimeter of the parallelogram is {} {}. ".format(perimeter_of_parallelogram, unit))
