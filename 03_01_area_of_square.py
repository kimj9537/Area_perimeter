
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

if shape_name == "square":
    side_length = num_check(" How long is the length of a side of the square? ")
    area_of_square = side_length * side_length
    perimeter_of_square = side_length * 4
    if user_choice == "both":
        print("The area of the square is {}".format(area_of_square))
        print("The perimeter of the square is {}".format(perimeter_of_square))
    elif user_choice == "area:":
        print("The area of the square is {}".format(area_of_square))
    elif user_choice == "perimeter":
        print("The perimeter of the square is {}".format(perimeter_of_square))
