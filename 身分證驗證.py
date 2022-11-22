def functionA(id):
    
    A = {'A': 1, 'B': 10, 'C': 19, 'D': 28, 'E': 37, 'F': 46,
            'G': 55, 'H': 64, 'I': 39, 'J': 73, 'K': 82, 'L': 2, 'M': 11,
            'N': 20, 'O': 48, 'P': 29, 'Q': 38, 'R': 47, 'S': 56, 'T': 65,
            'U': 74, 'V': 83, 'W': 21, 'X': 3, 'Y': 12, 'Z': 30}

    sum = A[id[0]] + int(id[1]) * 8 + int(id[2]) * 7 + int(id[3]) * 6 + int(id[4]) * 5 + int(id[5]) * 4 + int(id[6]) * 3 + int(id[7]) * 2 + int(id[8]) * 1 + int(id[9])

    if sum % 10 == 0:
        print("CORRECT")
    else:
        print("WRONG")


id = str(input(""))
functionA(id)