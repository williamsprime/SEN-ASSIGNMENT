 # Initialize variables
total_credit_units = 0
total_credit_points = 0
grade_point_scale = {'A': 5.0, 'B': 4.0, 'C': 3.0, 'D': 2.0, 'E': 1.0, 'F': 0.0}

# Function to calculate the credit points for a course
def calculate_credit_points(credit_unit, grade):
    return credit_unit * grade_point_scale[grade]

# Main function to calculate the SGPA
def calculate_sgpa():
    global total_credit_points, total_credit_units
    # Request user input for the number of courses
    num_courses = int(input("Enter the number of courses: "))

    # Iterate through each course
    for i in range(num_courses):
        # Request user input for the course name, credit unit, and grade
        course_name = input(f"Enter the name of course {i+1}: ")
        credit_unit = int(input(f"Enter the credit unit of course {i+1}: "))
        grade = input(f"Enter the grade of course {i+1} (A to F): ").upper()

        # Validate the inputs
        if credit_unit < 1 or credit_unit > 5:
            print("Invalid credit unit. Please enter a value between 1 and 5.")
            return
        if grade not in grade_point_scale:
            print("Invalid grade. Please enter a value between A to F.")
            return

        # Calculate the credit points for the course
        credit_points = calculate_credit_points(credit_unit, grade)

        # Update the total credit points and units
        total_credit_points += credit_points
        total_credit_units += credit_unit

    # Calculate the SGPA
    sgpa = total_credit_points / total_credit_units

    # Display the SGPA
    print(f"The SGPA is: {sgpa}")

# Call the main function
calculate_sgpa()

