def PowTwoGen(max=0):
    n=0
    while n<max:
        yield 2**n
        n+=1
for n in PowTwoGen(3):
    print(n)