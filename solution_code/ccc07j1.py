#ccc07j1 Who is in the middle?

a = int(input(''))
b = int(input(''))
c = int(input(''))

inp = list([a, b, c])
inp.sort()
print(inp[1])

#assert(bowl(50, 76, 8)) == 50
#assert(bowl(85, 75, 7)) == 75



def bowl(w: int, c: int, m: int) ->int:
    #print(w, c ,m)
    #52 10 76
    if w > c and w < m:
        return w
    if m > c and m < w:
        return m
    if c > w and c < m:
        return c
