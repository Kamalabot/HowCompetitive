#Programm CC's Satisfaction dmopc16c1p0

w = float(input(''))
c = float(input(''))
#M = ''

def chesse(w: int, c: int) ->str:
    
    if w == 3 and c >= 95: # w = 3 and c atleast 95%
        return 'absolutely'

    if w == 1 and c <= 50: # w = 1 and c atmost 50%
        return 'fairly'
    
    if w == 2 and c > 0 or c < 100:
        return 'very'

    if w == 3 and c < 95: # w = 1 and c atmost 50%
        return 'very'

    if w == 1 and c > 50 or c <= 100:
        return 'very'

M = chesse(w, c) 

"""
if w >= 1 and w < 3 and c >= 95:
    M = 'very'

if w > 1 and w < 3 and c <= 50:
    M = 'very'

elif  w == 3 and c > 50 and c < 95:
    M = 'very'
#elif (w >= 1 and w < 3) and (c > 50):
"""    

print(f"C.C. is {M} satisfied with her pizza.")
