import math

def num_check(question):

    error = "Please enter ACTUAL valid numbers that can be a length of a radius. "
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



radius = num_check(" How long is the radius? ")

area_of_circle = radius * radius * math.pi

print(area_of_circle)