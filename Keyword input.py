if choice == '1':
    # Hard-coded coefficients for a quadratic equation representing a weather model
    a = 2
    b = -7
    c = 3
    solutions = solve_weather_equation(a, b, c)
    print("Solutions:", solutions)
    plot_weather_model(a, b, c)
   
elif choice == '2':
    # Take coefficients from user input
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    solutions = solve_weather_equation(a, b, c)
    print("Solutions:", solutions)
    plot_weather_model(a, b, c)
   
elif choice == '3':
    try:
        filename = input("Enter the file name with coefficients (e.g., coefficients.txt): ")
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                coefficients = list(map(float, line.split()))
                a, b, c = coefficients
                solutions = solve_weather_equation(a, b, c)
                print(f"Coefficients: {coefficients} -> Solutions: {solutions}")
                plot_weather_model(a, b, c)
    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")
   
else:
    print("Invalid choice. Please select 1, 2, or 3.")
