import math

def calculator():
    print("=== Python Calculator ===")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponent (^)")
    print("6. Root (√)")
    print("7. Trigonometry (sin, cos, tan)")
    print("8. Exit")

    while True:
        choice = input("\nChoose operation (1-8): ")

        if choice == "8":
            print("Exiting calculator... Goodbye!")
            break

        # Multiple numbers input for arithmetic
        if choice in ["1", "2", "3", "4"]:
            nums = input("Enter numbers separated by space: ").split()
            nums = [float(x) for x in nums]

            if choice == "1":  # Addition
                print("Result:", sum(nums))

            elif choice == "2":  # Subtraction
                result = nums[0]
                for n in nums[1:]:
                    result -= n
                print("Result:", result)

            elif choice == "3":  # Multiplication
                result = 1
                for n in nums:
                    result *= n
                print("Result:", result)

            elif choice == "4":  # Division
                result = nums[0]
                try:
                    for n in nums[1:]:
                        result /= n
                    print("Result:", result)
                except ZeroDivisionError:
                    print("Error: Division by zero!")

        # Exponent (two numbers only: base ^ power)
        elif choice == "5":
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result:", a ** b)

        # Root (any root)
        elif choice == "6":
            number = float(input("Enter number: "))
            n = float(input("Enter root (e.g., 2 for square root, 3 for cube root): "))
            if n != 0:
                result = number ** (1/n)
                print("Result:", result)
            else:
                print("Error: Root cannot be zero!")

        # Trigonometry
        elif choice == "7":
            func = input("Choose function (sin, cos, tan): ").lower()
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)  # Convert to radians
            if func == "sin":
                print("Result:", math.sin(rad))
            elif func == "cos":
                print("Result:", math.cos(rad))
            elif func == "tan":
                print("Result:", math.tan(rad))
            else:
                print("Invalid trig function!")

        else:
            print("Invalid choice, try again!")

# Run the calculator
calculator()
