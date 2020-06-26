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


height_length = num_check(" How long is the height of this triangle? ")
base_length = num_check(" How long is the base of the triangle? ")

area_of_triangle = height_length * base_length * 0.5

print("The area of the triangle is {}".format(area_of_triangle))