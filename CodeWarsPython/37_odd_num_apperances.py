def find_it(seq):
    while True:
        count = 0
        for t in range(len(seq)):
            if seq[t] == seq[0]:
                count += 1
        if count % 2 == 1:
            return seq[0]
        seq.append(seq[0])
        seq.pop(0)

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))