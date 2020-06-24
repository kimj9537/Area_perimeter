def num_check(question, question2):

    error = "Please enter ACTUAL valid numbers that can be a side of a rectangle. "
    error1 = "Please enter a number that is more than zero. "
    error2 = "Please enter ACTUAL valid numbers that can be a height of a rectangle. "
    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error1)

            elif response == 0:
                print(error1)
            else:

                return response

        except ValueError:
            print(error)
    while not valid:
        try:
            response = float(input(question2))

            if response <= 0:
                print(error2)

            elif response == 0:
                print(error2)
            else:

                return response

        except ValueError:
            print(error)




side_length = num_check(" How long is the side of the rectangle? ")
height_length = num_check(" How long is the height of the rectangle? ")

perimeter_of_square = side_length * height_length

print("The area of the square is {}".format(perimeter_of_square))