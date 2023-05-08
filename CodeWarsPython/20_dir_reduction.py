def dirReduc(arr):
    m = 0
    while True:
        prev = "null"
        comp1 = arr.copy()
        for idx, direction in enumerate(arr):
            if direction == "SOUTH" and prev == "NORTH":
                arr.pop(idx)
                arr.pop(idx-1)
            elif direction == "NORTH" and prev == "SOUTH":
                arr.pop(idx)
                arr.pop(idx-1)
            elif direction == "WEST" and prev == "EAST":
                arr.pop(idx)
                arr.pop(idx-1)
            elif direction == "EAST" and prev == "WEST":
                arr.pop(idx)
                arr.pop(idx-1)
            prev = direction
        comp2 = arr.copy()
        if comp1 == comp2 and m > 0:
            break
        m = m + 1
    return arr

print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))