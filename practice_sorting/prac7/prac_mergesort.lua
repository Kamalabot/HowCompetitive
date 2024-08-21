-- from typing import List

-- # intuition 1: do sorting if list len is greate than 1, else return list
-- # intuition 2: divide the list into left and right at the mid point, recursively sort
-- # intuition 3: while left and right lists have elements to sort,
-- # compare each element, and assign the smallest to original array
-- # above intuition is checked by creating i, j, k = 0 and incremementing them after
-- # every comparison operator
-- # intuition 4: while there are more elements present in left / right list, then
-- # assign them individually to original array


local function merge_sort(in_list)
  local mylist = in_list
  if #mylist > 1 then
    local mid = math.floor(#mylist / 2)
    print("Mid value is: " .. mid)
    local left = unpack(mylist, 1, mid)
    for key, val in pairs(left) do
      print("Key: " .. key .. " : " .. val)
    end
  end
end

local in_array = {1, 8, 7, 9, 0, 12, 15, 78, 68, 36}

print(table.concat(in_array, ","))

local unpack_array = table.unpack(in_array  )
print(type(unpack_array))

-- print("Unpacked sub array: " .. table.concat(unpack_array, ","))
print("Unpacked sub array: " .. unpack_array)

-- local sorted_array = merge_sort(in_array)

