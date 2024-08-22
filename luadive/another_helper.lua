_G.another_helper = {}

function GenFiles()
  io.output("food.txt")
  for i = 0, 10 do
    io.write(i)
  end
  io.close()
end

function Cleanup()
  os.execute("rm *.txt")
end

return another_helper
