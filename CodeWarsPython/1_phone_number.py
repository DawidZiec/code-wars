# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
    return str("("+str(n[0])+str(n[1])+str(n[2])+") "+str(n[3])+str(n[4])+str(n[5])+"-"+str(n[6])+str(n[7])+str(n[8])+str(n[9]))

create_phone_number([1, 2, 3, 5, 4, 1, 7, 9, 2, 7])