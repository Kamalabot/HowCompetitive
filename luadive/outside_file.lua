_G.hello = "This is nice..."

print(type(_G.hello))

print(tonumber('66'))

local var = 568 * 68

print("The product of 568 and 68 is " .. var ..".")

print(5 * 2 + 10) -- 20

print(5 * 2 + 10 / 2) -- 15.0
print(((5 * 2) + 10)/ 2) -- 15.0

print(math.pi)
print("random: " .. math.random())

print("Os Time: " .. os.time())

print("random: 10 to 50 " .. math.random(10, 75))

print(math.max(3, 6, 5, 7, 8, 1))
print(math.min(3, 6, 5, 7, 8, 1))

print(math.floor(3.888675))

-- strings
local str = "Hello Worcd"

print(#str)

print(str .. " there")

print("Hello\nWorld\n....\v I am Kamal")

print(string.lower("sUperMario"))
print(string.upper("sUperMario"))
print(string.len("sUperMario"))
print(string.sub("sUperMario", 5,8))

print(string.char(66)) -- Number 
print(string.byte("c")) -- byte 
print(string.tonumber("c")) -- byte 
-- print(string.char("a"))

