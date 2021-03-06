import math


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

radius = num_check(" How long is the radius? ")

perimeter_of_circle = radius * 2 * math.pi

print("The perimeter of the circle is {}".format(perimeter_of_circle))