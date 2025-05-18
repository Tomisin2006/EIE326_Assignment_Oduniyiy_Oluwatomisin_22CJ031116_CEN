def gpa():
    print("Enter the grade points for 6 courses ")
    
    total_points = 0
    total_units = 0
    
    for i in range(1, 7):
        try:
            unit = int(input(f"Enter credit units for course {i}: "))
            grade = input(f"Enter letter grade for course {i} (A-F): ")
            
            grade_points = {
                'A': 5.0,
                'B': 4.0,
                'C': 3.0,
                'D': 2.0,
                'E': 1.0,
                'F': 0.0,
            }
            
            if grade not in grade_points:
                print("Invalid grade entered. Please use A-F only.")
                return
            
            total_points += grade_points[grade] * unit
            total_units += unit
        except ValueError:
            print("Invalid input. Please enter numeric values for units.")
            return

    if total_units == 0:
        print("Total credit units cannot be zero.")
        return

    gpa = total_points / total_units
    print(f"Student GPA:,  {gpa:.2f}")

gpa()
