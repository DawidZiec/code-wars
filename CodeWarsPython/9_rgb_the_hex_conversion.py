'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''
import math


def rgb(r, g, b):
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255

    hex_string = ''

    first_v = r / 16
    if math.floor(first_v) == 10:
        hex_string = hex_string+'A'
    elif math.floor(first_v) == 11:
        hex_string = hex_string+'B'
    elif math.floor(first_v) == 12:
        hex_string = hex_string+'C'
    elif math.floor(first_v) == 13:
        hex_string = hex_string+'D'
    elif math.floor(first_v) == 14:
        hex_string = hex_string+'E'
    elif math.floor(first_v) == 15:
        hex_string = hex_string+'F'
    else:
        hex_string = hex_string+str(math.floor(first_v))

    second_v = (first_v - math.floor(first_v)) * 16
    if math.floor(second_v) == 10:
        hex_string = hex_string+'A'
    elif math.floor(second_v) == 11:
        hex_string = hex_string+'B'
    elif math.floor(second_v) == 12:
        hex_string = hex_string+'C'
    elif math.floor(second_v) == 13:
        hex_string = hex_string+'D'
    elif math.floor(second_v) == 14:
        hex_string = hex_string+'E'
    elif math.floor(second_v) == 15:
        hex_string = hex_string+'F'
    else:
        hex_string = hex_string+str(math.floor(second_v))

    third_v = g / 16
    if math.floor(third_v) == 10:
        hex_string = hex_string+'A'
    elif math.floor(third_v) == 11:
        hex_string = hex_string+'B'
    elif math.floor(third_v) == 12:
        hex_string = hex_string+'C'
    elif math.floor(third_v) == 13:
        hex_string = hex_string+'D'
    elif math.floor(third_v) == 14:
        hex_string = hex_string+'E'
    elif math.floor(third_v) == 15:
        hex_string = hex_string+'F'
    else:
        hex_string = hex_string+str(math.floor(third_v))

    fourth_v = (third_v - math.floor(third_v)) * 16
    if math.floor(fourth_v) == 10:
        hex_string = hex_string+'A'
    elif math.floor(fourth_v) == 11:
        hex_string = hex_string+'B'
    elif math.floor(fourth_v) == 12:
        hex_string = hex_string+'C'
    elif math.floor(fourth_v) == 13:
        hex_string = hex_string+'D'
    elif math.floor(fourth_v) == 14:
        hex_string = hex_string+'E'
    elif math.floor(fourth_v) == 15:
        hex_string = hex_string+'F'
    else:
        hex_string = hex_string+str(math.floor(fourth_v))

    fifth_v = b / 16
    if math.floor(fifth_v) == 10:
        hex_string = hex_string+'A'
    elif math.floor(fifth_v) == 11:
        hex_string = hex_string+'B'
    elif math.floor(fifth_v) == 12:
        hex_string = hex_string+'C'
    elif math.floor(fifth_v) == 13:
        hex_string = hex_string+'D'
    elif math.floor(fifth_v) == 14:
        hex_string = hex_string+'E'
    elif math.floor(fifth_v) == 15:
        hex_string = hex_string+'F'
    else:
        hex_string = hex_string+str(math.floor(fifth_v))

    sixth_v = (fifth_v - math.floor(fifth_v)) * 16
    if math.floor(sixth_v) == 10:
        hex_string = hex_string+'A'
    elif math.floor(sixth_v) == 11:
        hex_string = hex_string+'B'
    elif math.floor(sixth_v) == 12:
        hex_string = hex_string+'C'
    elif math.floor(sixth_v) == 13:
        hex_string = hex_string+'D'
    elif math.floor(sixth_v) == 14:
        hex_string = hex_string+'E'
    elif math.floor(sixth_v) == 15:
        hex_string = hex_string+'F'
    else:
        hex_string = hex_string+str(math.floor(sixth_v))

    return hex_string


print(rgb(220, 200, 50))
