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

base_length = num_check(" How long is the base of this parallelogram? ")
height_length = num_check(" How long is the height of this parallelogram? ")

perimeter_of_parallelogram = (base_length + height_length) * 2

print("The area of this parallelogram is {}".format(perimeter_of_parallelogram))