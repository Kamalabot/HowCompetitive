local function Pet(name) 
  name = name or "Luis"
  return {
    name = name,
    status = "Hungry",

    feed = function(self)
      print(self.name .. " " .. " is fed.")
      self.status = "Full"
    end
  }
end

local cat = Pet("Kitty")
print(cat.status)
cat:feed()
print(cat.status)


local function Dog(name, breed)
  local dog = Pet(name)
  dog.breed = breed
  dog.loyalty = 0

  dog.isLoyal = function (self)
    return self.loyalty >= 0
  end

  dog.bark = function (self)
    return "woof woof"
  end

  return dog -- this return is important

end

local lassy = Dog("Layyy", "poodle")

print(lassy:bark())

print(lassy:isLoyal())

