from itertools import permutations

# Letters in puzzle
letters = ('S','E','N','D','M','O','R','Y')

# Try all possible digit permutations
for perm in permutations(range(10), 8):
    S,E,N,D,M,O,R,Y = perm
    
    # First digit cannot be zero
    if S == 0 or M == 0:
        continue
    
    # Form numbers
    SEND = 1000*S + 100*E + 10*N + D
    MORE = 1000*M + 100*O + 10*R + E
    MONEY = 10000*M + 1000*O + 100*N + 10*E + Y
    
    # Check constraint
    if SEND + MORE == MONEY:
        print("Solution Found:")
        print(f"S={S}, E={E}, N={N}, D={D}")
        print(f"M={M}, O={O}, R={R}, Y={Y}")
        print(f"{SEND} + {MORE} = {MONEY}")
        break
