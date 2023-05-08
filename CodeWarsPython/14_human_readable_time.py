'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''

from math import floor

def make_readable(seconds):
    secs = seconds % 60
    rest_secs = floor(seconds / 60)
    mins = rest_secs % 60
    rest_mins = floor(rest_secs / 60)
    hours = rest_mins % 100

    print(str(hours).zfill(2)+":"+str(mins).zfill(2)+":"+str(secs).zfill(2))

make_readable(36000)