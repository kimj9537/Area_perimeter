
error = "This kind of shape isn't added to this program or not existing."







def name_checker(question, error_msg, letter_ok):


    valid = False
    while not valid:
        response = input(question)
        has_errors = ""
        if letter_ok != "yes":
            for number in response:
                if number.isdigit():
                    has_errors = "yes"
                    break
            if response == name_checker(question)





    name_tocheck = input("What is the name of the shape? ")

    circle = ["Circle", "c", "C", "O", "o", "circle"]
    square = ["square", "Square", "s", "S"]
    rectangle = ["rectangle", "Rectangle", "r", "R", "rec", "Rec"]
    triangle = ["triangle", "Triangle", "T", "t", "tri", "Tri"]
    parallelogram = ["parallelogram", "Parallelogram"]

    elif name_tocheck == "C" or name_tocheck.lower() in circle:
        return "circle"
    elif name_tocheck.lower() in square:
        return "square"
    elif name_tocehck.lower() in 




# keep_going = ""

