import math

def volume_of_sphere(radius):
    return (4 / 3) * math.pi * radius**3

def main():
    radius = float(input("Enter the radius: "))
    result = volume_of_sphere(radius)
    print("The volume of the sphere is:", result)

if __name__ == "__main__":
    main()
