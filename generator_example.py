#generator function that produces a sequence of numbers
def generator_name(arg):
    #stmt
    yield something
def my_generator(n):
    #initialize counter 
    value =0
    #loop until counter is less than n 
    while value < n:
        #produce the current value of the counter
        yield value# increment the counter
        value +=1
        
#iterate over the generator object produced by my_generator
for value in my_generator(3):
    #print each value produced by geneartor
    print(value)
        