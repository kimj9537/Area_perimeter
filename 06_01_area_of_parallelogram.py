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

area_of_parallelogram = base_length * height_length

print("The area of this parallelogram is {}".format(area_of_parallelogram))