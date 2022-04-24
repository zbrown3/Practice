walls = [(20, 9), (25, 9), (20, 9), (25, 9)]


def calc_paint_amount(wall_measurements):
    square_feet = 0

    def calc_square_feet():
        for width, height in wall_measurements:
            nonlocal square_feet
            square_feet += width * height

    def calc_gallons():
        return square_feet / 400

    calc_square_feet()

    return calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(walls)))

"""
The nonlocal statement  provides a way for us to modify names in the enclosing scope.
"""