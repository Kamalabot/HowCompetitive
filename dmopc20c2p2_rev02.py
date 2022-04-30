lst = input().split()

n = int(lst[0])

q = int(lst[1])

strokes = []

for i in range(q):

    stroke = input().split()

    strokes.append([int(stroke[0]), int(stroke[1])])

strokes.sort()

rightmost_position = 0

blue = 0

for stroke in strokes:

    stroke_start = stroke[0]
    
    stroke_end = stroke[1]
    
    if stroke_start <= rightmost_position:
    
        if stroke_end > rightmost_position:
    
            blue = blue + stroke_end - rightmost_position
            
            rightmost_position = stroke_end
    else:
        
        blue = blue + stroke_end - stroke_start
        
        rightmost_position = stroke_end

print(n - blue, blue)