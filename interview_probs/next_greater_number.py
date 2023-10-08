def nextGreater(num):
  # we create a list named digits to store digits of num
  digits = list(str(num))

  # we create and initialize i to the before last index 
  # (because the last element has no next element
  # so digits[i+1] doesn't exist)
  i = len(digits) - 2
  # we search for the element that breaks the ascending order
  while i >= 0 and digits[i] >= digits[i+1]:
    i -= 1
  # if we find -1, then the next greater doesn't exist, we return num
  if i == -1:
    return num
  
  # we create and initialize j to the last index
  j = len(digits) - 1
  # we search for the first digit that is greater than digits[i]
  while digits[j] <= digits[i]:
    j -= 1

  # we swap digits[i] with digits[j]
  digits[i], digits[j] = digits[j], digits[i]

  # we reverse the part that starts from i+1
  digits[i+1:] = digits[:i:-1]
  
  # we return digits as an integer
  return int("".join(digits))