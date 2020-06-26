import math

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

radius = num_check(" How long is the radius? ")

area_of_circle = radius * radius * math.pi

print("The area of the circle {}".format(area_of_circle))