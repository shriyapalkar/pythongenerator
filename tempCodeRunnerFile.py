#create a generator which returns square 0f the no as well as fibo series

def fibo(nums):
    x,y=0,1
    for _ in range (nums):
       x,y=y,x+y
       yield x
def square(nums):
    for num in nums:
        yield num**2 
print(fibo(5))
print(sum(square(fibo(5))))
    
    