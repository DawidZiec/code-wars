def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    coordinates = [0, 0]
    for dir in walk:
        if dir == 'w':
            coordinates[0] += 1
        if dir == 'e':
            coordinates[0] -= 1
        if dir == 'n':
            coordinates[1] += 1
        if dir == 's':
            coordinates[1] -= 1
    if coordinates == [0, 0]:
        return True
    else:
        return False

print(is_valid_walk(['w', 'e', 'w', 'e', 's', 'n', 'w', 'e', 'e', 'w']))