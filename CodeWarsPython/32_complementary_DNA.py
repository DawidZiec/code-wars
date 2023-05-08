def DNA_strand(dna):
    tempa = dna.replace('T', 'B')
    tempb = tempa.replace('A', 'T')
    tempc = tempb.replace('B', 'A')
    tempd = tempc.replace('C', 'D')
    tempe = tempd.replace('G', 'C')
    tempf = tempe.replace('D', 'G')
    return tempf