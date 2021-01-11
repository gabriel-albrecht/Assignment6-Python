#!/usr/bin/env python3

# Created by Gabriel A
# Created on Jan 2021
# This program calculates the volume of a cone

import math


def calculate_volume(radius, height):
    # calculates the volume of a cone

    number = math.pi * radius ** 2 * (height / 3)

    return number


def main():
    # input the radius and height
    print("Hi\nWe will be calculating the volume of a cone!\n")

    while True:
        try:
            radius_from_user = float(input("Enter the radius of a cone "
                                           "(cm): "))
            height_from_user = float(input("Enter the height of a cone "
                                           "(cm): "))
            print("")

            # calls function
            float_volume = calculate_volume(radius_from_user,
                                            height_from_user)
            cone_volume = "{:.2f}".format(float_volume)

            if radius_from_user <= 0 or height_from_user <= 0:
                print("Invalid input\n")
            else:
                # output
                print("The volume is: {0} cm³".format(cone_volume))
                break

        except ValueError:
            print("\nYou entered an invalid key.\nTry again.\n")


if __name__ == "__main__":
    main()
