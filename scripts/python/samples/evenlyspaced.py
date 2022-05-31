def space(a,b,c):
    numbers= [a,b,c]
    mayor=0
    #ordenación
    numbers.sort(key=None, reverse=False)
    #comparacion
    return  (numbers[0]-numbers[1]==numbers[1]-numbers[2])

print(space(2,4,8))