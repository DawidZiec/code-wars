def recoverSecret(triplets):

    # list prep
    worklist = []

    # filling the list with every character
    for triplet in triplets:
        if triplet[0] not in worklist:
            worklist.append(triplet[0])
        if triplet[1] not in worklist:
            worklist.append(triplet[1])
        if triplet[2] not in worklist:
            worklist.append(triplet[2])

    # putting characters in order // worklist.index(order[n])
    while True:
        changes = 0
        for order in triplets:
            if worklist.index(order[0]) > worklist.index(order[1]):
                temp = worklist[worklist.index(order[0])]
                worklist[worklist.index(order[0])] = worklist[worklist.index(order[1])]
                worklist[worklist.index(order[1])] = temp
                changes += 1
            if worklist.index(order[0]) > worklist.index(order[2]):
                temp = worklist[worklist.index(order[0])]
                worklist[worklist.index(order[0])] = worklist[worklist.index(order[2])]
                worklist[worklist.index(order[2])] = temp
                changes += 1
            if worklist.index(order[1]) > worklist.index(order[2]):
                temp = worklist[worklist.index(order[1])]
                worklist[worklist.index(order[1])] = worklist[worklist.index(order[2])]
                worklist[worklist.index(order[2])] = temp
                changes +=1
        if changes == 0: break
        result = ""
        for char in worklist:
            result = result + char
    return result


triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))