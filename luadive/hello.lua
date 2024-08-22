print("Hello World...")

print('Mostly good')

local one = 1
print("THis is one: " .. one)

while one > -5 do
  print("this is going reverse " .. one)
  one = one - 1
  -- if one < -5 then
  --   break
  -- end
end

local function print_tab(table)
  for key, val in pairs(table) do
    print(key, val)
  end
end

local t = {'a', 'b', 'c'}

print_tab(t)

local t1 = {mykey='a', 'b', 'c'}

print_tab(t1)

print(t1.mykey)
-- 'b' starts with 1
