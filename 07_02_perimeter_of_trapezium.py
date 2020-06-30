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
side_C_length = num_check(" How long is the side C of this trapezium? ")
side_D_length = num_check(" How long is the side D of this trapezium? ")

perimeter_of_trapezium = base_A_length + base_B_length + side_C_length + side_D_length

print("The perimeter of this trapezium is {}".format(perimeter_of_trapezium))