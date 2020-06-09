import math

def num_check(question):

    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:

                return response

        except ValueError:
            print (error)



radius = num_check(" How long is the radius? ")
    if radius < 0:
        dodgy_sf = input("The length of the radius has to be bigger than 0.").lower()
    if radius = 0:
        dodgy_sf = input("The length has to be a positive number with certain amount.").lower()

area_of_circle = radius * radius * math.pi


print(area_of_circle(1))