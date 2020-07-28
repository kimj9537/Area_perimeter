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

side_A_length = num_check(" How long is the side A of this parallelogram? ")
side_B_length = num_check(" How long is the side B of this parallelogram? ")
side_C_length = num_check(" How long is the side C of this parallelogram? ")
side_D_length = num_check(" How long is the side D of this parallelogram? ")

perimeter_of_parallelogram = side_A_length + side_B_length + side_C_length + side_D_length

print("The perimeter of this parallelogram is {}".format(perimeter_of_parallelogram))