# from typing import List
local hmod = require("helper")

-- # intuition 1: loops over the entire list twice
-- # intuition 2: 2nd loop leaves the last element, from where
-- # the actual sorting / bubbling starts to occur
-- # intuition 3: swapped if next element is smaller than current
-- # in lua the list starts at 1


local function bubble_sort(in_list)
  local my_list = in_list
  -- require local list variable to do the sorting and then returning
  -- global variables don't get affected by what is done inside function
  local n = #my_list
  -- print("len is" .. n)
  for i = 1, n do
    -- print("i val is: " .. i)
    for j = 1, (n - i) do
      -- print("j val is: " .. j)
      if my_list[j] > my_list[j + 1] then
        print("entering if..")
        my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
      end
    end
  end
  -- print("Printing here..." .. my_list[1])
  -- print("Printing here..." .. my_list[2])
  return my_list
end


local in_array = {1, 8, 7, 9, 0, 12, 15, 78, 68, 36}

-- in_array[6] = 25

-- print(in_array[6])
-- print(in_array[1])

-- print(hmod.TestVar)

function Print_list(in_list)
  print("Entering Print...")
  for key, val in pairs(in_list) do
    print(key .. " : " .. val)
  end
end

Sorted_array = bubble_sort(in_array)

Print_list(Sorted_array)

