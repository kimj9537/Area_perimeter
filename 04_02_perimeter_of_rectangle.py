def num_check(question):

    error = "Please enter a number that is more than zero. "

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response < 0:
                print(error)

            else:

                return response

        except ValueError:
            print(error)


side_length = num_check(" How long is the side of the rectangle? ")
height_length = num_check(" How long is the height of the rectangle? ")

perimeter_of_rectangle = (side_length + height_length) * 2

print("The area of the square is {}".format(perimeter_of_rectangle))