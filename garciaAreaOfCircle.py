import math

def garcia_calculate_circle_area():
    print("=" * 40)
    print("     Circle Area Calculator")
    print("=" * 40)

    garciarad = float(input("Enter the radius of the circle: "))

    garciaarea = math.pi * garciarad ** 2

    print(f"\nRadius: {garciarad}")
    print(f"Area: {garciaarea:.2f} square units")


garcia_calculate_circle_area()