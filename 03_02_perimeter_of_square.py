def num_check(question):

    error = "Please enter ACTUAL valid numbers that can be a length of a square. "
    error1 = "Please enter a number that is more than zero. "

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



side_length = num_check(" How long is the length of a side of the square? ")

perimeter_of_square = side_length * 4

print("The area of the square is {}".format(perimeter_of_square))