def square(x):
  return x*x

nums = [1,2,3,4,45]
sqlist = map(lambda x:x*x,nums)
print(list(sqlist))

# Another Method
nums = [1,2,3,4,45]
sqlist = map(square,nums)
print(next(sqlist)) #1
print(next(sqlist)) #4
print(next(sqlist)) #9
print(next(sqlist)) #16

# Making Changes
square = lambda x: x**2
square_of_list = list(map(square,[1,2,3,4]))
print(square_of_list)