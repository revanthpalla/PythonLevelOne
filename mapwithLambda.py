nums = [1,2,3,4,45]
sqlist = map(lambda x:x*x,nums)
print(list(sqlist))

#also we can write same like this

def square(x):
  return x*x
nums = [1,2,3,4,45]
sqlist = map(square,nums)
print(next(sqlist)) #1
print(next(sqlist)) #4
print(next(sqlist)) #9
print(next(sqlist)) #16
