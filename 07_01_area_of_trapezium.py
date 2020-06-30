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

base_A_length = num_check(" How long is the base A of this trapezium? ")
base_B_length = num_check(" How long is the base B of this trapezium? ")
height_length = num_check(" How long is the height of this trapezium? ")

area_of_trapezium = (base_A_length + base_B_length) * 0.5 * height_length

print("The area of this trapezium is {}".format(area_of_trapezium))