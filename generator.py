def gencubes(n):

    for num in range(n):
        yield num**3
for i in gencubes(10):
    print(i)