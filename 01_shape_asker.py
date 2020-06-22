
def shape_checker(question, to_check):

    valid = False
    while not valid:

        response = input(question).lower()

        for shape in to_check:
            if response == shape:
                return response
            elif response == shape[0]:
                return shape

        print("That isn't a proper name for a shape.")

# *** Main Routine ****

shape_name = ["circle", "square", "rectangle", "triangle", "parallelogram"]

shape_name = shape_checker("What is the name of the shape?", shape_name)
print(shape_name)