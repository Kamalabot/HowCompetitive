local a = "HEllo Wordl"

print(a)

A = [[
  "There is more",
  "to Lua than int ",
  "meetts the eye"
]]

print(A)

-- the above A can be accessed from outside also
-- but seems to be not working
--
local tab1 = {nwew1= "one", new2="two"}
print(tab1.new2)

print(math.abs(-5))

local numbers = {5, 6, 7, 1, 2, 5, 7}
print(type(numbers))
print(math.max(5, 6, 7, 6))

print(string.sub(A, 6, 15))

do
  local namere = "thersodthe"
  print(namere)
end

local function do_print(namef)
  print("Hey there" .. namef)
end

do_print("theree")

GetAge = function()
  print("variablized function")
end

GetAge()

-- function can be passed as parameters

Do_funk = function(name, func)
  print("Your name is " .. name)
  func()
end

Do_funk("thers", GetAge)

Unknown_fnun = function(...)
  print("Cannot become more Unknown_fnun than this...", ...)
end

Unknown_fnun("thers")

table_fun = function(...)
  local args = {...} -- we are wrapping it into a table
  print(args[1])
  print(args[2])
  print(args[3])
end

table_fun(5, 6, 7)
table_fun(5, 6)

table_for = function(...)
  local args = {...} -- we are wrapping it into a table
  for i, v in pairs(args) do
    print(i .. " : " .. v)
  end
end

table_for(5, 6, 7)
table_for(5, 6)

retur_table = function()
  -- returning single arg
  return {"one", "two", "three"}
end

retur_multi = function()
  -- returning single arg
  return "one", "two", "three"
end


print(retur_table())
print(retur_table()[1])

local t2, t3, t4 = retur_multi()
print(t2, t3, t4)

-- if .. elseif .. else construct
-- while true do ... end 
-- repeat .. until true 
--
print("Give your name: ")
-- io.write can be used instead of print
-- local name = io.read()
-- print(name)

-- table.sort, table.concat, table.remove 
--
-- print(#name)
print(#retur_table())

-- os.execute, os.clock, os.remove
os.remove("text.txt")

-- env vars
local db_url = os.getenv("PHOENIX_SQL_DATABASE_URL")
print(db_url)

-- working with file is very interesting
io.output("newtext.txt")
io.write("This a data going to be writtent to newfile.txt\n")
io.close()
-- Opening a file that is already available

local newdata = io.open("newtext.txt", 'r')
for line in newdata:lines() do
  print(line)
end
newdata:close()

-- Start = (os.time())
-- print(Start)
-- for i = 0, 1000000 do
--   print(i)
-- end
-- End = os.time()
-- print(End)

-- print(End - Start)

-- importing modules
--
local h = require("helper")

h.GenFiles()
h.Cleanup()

print(h.TestVar)

local newtbl = {5, 6, 67}

table.insert(newtbl, 'lol')

for i = 0, #newtbl do
  print(newtbl[i])
end

-- concepts of coroutines were intro in Full Lua Programming Crash Course - Beginner to Advanced [1srFmjt1Ib0]
--
-- *line, *all, *number with io.read()
